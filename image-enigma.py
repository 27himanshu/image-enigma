# -*- coding: utf-8 -*-
"""
@author: himanshu
"""
import scipy.misc as misc
import enigma
import keys
from skimage import data            #for colored lena

"""Encrypting Grayscale Lena"""
e = enigma.Enigma((0, 0), keys.w_rotor1, keys.w_rotor2, keys.w_reflector, 
                  keys.w_plugboard, bpp=8)
image=misc.lena()
save_as="/home/user/encrypted_gray_lena.png"
e_image = e.cipher_image(image)
misc.imsave(save_as, e_image)
                  
                  
"""Decrypting Grayscale Lena"""
save_as="/home/user/unencrypted_gray_lena.png"
e = enigma.Enigma((0, 0), keys.w_rotor1, keys.w_rotor2, keys.w_reflector, 
                  keys.w_plugboard, bpp=8)
une_image=e.cipher_image(e_image)
misc.imsave(save_as, une_image)

"""Encrypting Colored Lena"""
e = enigma.Enigma((0, 0), keys.w_rotor1, keys.w_rotor2, keys.w_reflector, 
                  keys.w_plugboard, bpp=8)
image=data.lena()
save_as="/home/user/encrypted_color_lena.png"
e_image = e.cipher_image(image)
misc.imsave(save_as, e_image)

"""Decrypting Colored Lena"""
save_as="/home/user/unencrypted_color_lena.png"
e = enigma.Enigma((0, 0), keys.w_rotor1, keys.w_rotor2, keys.w_reflector, 
                  keys.w_plugboard, bpp=8)
une_image=e.cipher_image(e_image)
misc.imsave(save_as, une_image)