# -*- coding: utf-8 -*-
"""
Enigma machine modified to work with image files (or rather any 2d array)

For an 8-bit image and 2 rotors we have 2*255*255=130050 combinations
With 10 pairs of plugboard wires we have C(255,2)*C(253,2)*C(251,2)...*C(235,2) = 144,344,660,914,893,408,208,528,832,440,536,336,416,008,344,832 possible combinations.
In total (with 10 pairs of plugboard wires and 2 rotors) there are 1.877202315198188773752E+52 combinations for initial setup of rotors and plugboard. 
However with only 10 pairs of plugboard wires we cannot generate enough entropy (or randomness) to completely encrypt the image,
therefore in this project I've used the maximum possible pairs of plugboard for an 8 bit image i.e. 256/2=128 pairs.

@author: himanshu
"""


class Rotor():

    """Create new rotors with wirings
    """

    def __init__(self, wiring, depth, is_reflector=False, offset=0):
        """ wiring: a list containing mapping of rotor
            is_reflector: True if the rotor act as a reflector (by default set
            to False)
            offset: current offset of rotor
            number_spin: store the number of times rotor is rotated"""
        self.length=2**depth-1
        self.wiring = wiring
        self.number_spin = 0
        self.is_reflector = is_reflector
        for _ in range(offset):
            self.spin()
        self.offset = offset
        return

    def spin(self):
        """call this function to spin/step forward the rotor """
        self.number_spin = self.number_spin+1
        if(self.number_spin > 255):
            self.number_spin = 0
        self.offset = self.offset+1
        if(self.offset > self.length):
            self.offset = 0
        self.wiring = self.wiring[self.length:]+self.wiring[:self.length]
        return

    def map_forward(self, i):
        """map element forward (right to left)"""
        return self.wiring[i]

    def map_backward(self, i):
        """map element backward (left to right)"""
        index = self.wiring.index(i)
        return index

    def map_reflect(self, i):
        """map element in reflector"""
        return self.wiring[i]



class Plugboard():

    def __init__(self, wiring):
        self.wiring = wiring
        return

    def map_forward(self, i):
        return self.wiring[i]

    def map_backward(self, i):

        index = self.wiring.index(i)
        return index
        
        
class Enigma():

    """Enigma machine with two rotors, one reflector and a plugboard.
    Takes five arguments of which last four are wiring settings for 2 rotors, a
    reflector and a plugboard.
    First argument is a tuple of two elements containing offset of two rotors"""

    def __init__(self, off, wiring1, wiring2, wiring3, wiring4, bpp):
        self.wiring1 = wiring1
        self.wiring2 = wiring2
        self.wiring3 = wiring3
        self.wiring4 = wiring4
        self.depth=bpp
        self.off = off
        self.r1 = Rotor(self.wiring1, offset=off[0], depth=bpp)
        self.r2 = Rotor(self.wiring2, offset=off[1], depth=bpp)
        self.r3 = Rotor(self.wiring3, is_reflector=True, depth=bpp)
        self.p1 = Plugboard(self.wiring4)

    def cipher(self, in_array):
        """Encode the list in_text and return the encoded list"""
        out_array = []
        for i in in_array:
            j = self.p1.map_forward(i)
            j = self.r1.map_forward(j)
            j = self.r2.map_forward(j)
            j = self.r3.map_reflect(j)
            j = self.r2.map_backward(j)
            j = self.r1.map_backward(j)
            j = self.p1.map_backward(j)
            out_array.append(j)
            self.r1.spin()
            if(self.r1.number_spin == 26):
                self.r2.spin()
        return out_array
        
    def cipher_image(self, image):
        """Encode an image file row-wise"""
        e_image=image[:]    #copying image to e_image
        if(len(image.shape) == 2):
            for i in range(image.shape[0]):
                e_image[i]=self.cipher(image[i])
        else:
            layers=image.shape[2]
            for i in range(layers):
                n_image=image[:,:,i]
                for j in range(n_image.shape[0]):
                    e_image[j,:,i]=self.cipher(n_image[j])
        return e_image
        
