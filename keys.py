# -*- coding: utf-8 -*-
"""
Read keys from config file
@author: himanshu
"""

import configparser
import json

config = configparser.ConfigParser()
config.read("keys.ini")

w_rotor1 = json.loads(config.get("keys", "w_rotor1"))
w_rotor2 = json.loads(config.get("keys", "w_rotor2"))
w_reflector = json.loads(config.get("keys", "w_reflector"))
w_plugboard = json.loads(config.get("keys", "w_plugboard"))