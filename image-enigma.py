# -*- coding: utf-8 -*-
"""
@author: himanshu
"""
import scipy.misc as misc
import enigma
import generator

e = enigma.Enigma((0, 0), generator.w_rotor1, generator.w_rotor2, generator.w_reflector, 
                  generator.w_plugboard, bpp=8)

"""Encrypting Lena"""
image=misc.lena()
save_as="/home/user/encrypted_lena.png"
e_image = e.cipher_image(image)
misc.imsave(save_as, e_image)
                  
"""Decrypting Lena"""
save_as="/home/user/unencrypted_lena.png"
e = enigma.Enigma((0, 0), generator.w_rotor1, generator.w_rotor2, generator.w_reflector, 
                  generator.w_plugboard, bpp=8)
une_image=e.cipher_image(e_image)
misc.imsave(save_as, une_image)