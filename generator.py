# -*- coding: utf-8 -*-
"""
Generate keys
Generate rotor, reflector and plugboard mappings.
Set depth variable to bits per pixle value and set generate_wiring to True
Keys are stored in keys.ini file
@author: himanshu

"""


import configparser
import numpy as np
depth=8

generate_wiring=True
def generate_wiring_rp(depth):
    """Generates wiring for reflector and plugboard """
    length=2**depth
    a=[i for i in range(length)]
    a=np.random.permutation(a).tolist()
    
    for i in range(256):
        t=a[i]
        t2=a.index(i)
        (a[t],a[t2])=(a[t2],a[t])
    return a
    
def generate_wiring(depth):
    """Generates wiring for rotors"""
    length=2**depth
    a=[i for i in range(length)]
    return np.random.permutation(a).tolist()

if(generate_wiring):
    config=configparser.ConfigParser()
    with open("keys.ini",'w') as keys:
        config.add_section("keys")
        config.set("keys", "w_rotor1", str(generate_wiring(depth)))
        config.set("keys", "w_rotor2", str(generate_wiring(depth)))
        config.set("keys", "w_reflector", str(generate_wiring_rp(depth)))
        config.set("keys", "w_plugboard", str(generate_wiring_rp(depth)))
        config.write(keys)
        