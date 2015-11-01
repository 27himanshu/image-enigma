# image-enigma


Using Enigma machine to encrypt images.  

For an 8-bit image and 2 rotors we have 2\*255\*255=130050 combinations  
Assuming fixed reflectros, that is wiring of reflector cannot be changed.  
Using a maximum possible pairs of plugboard wires (128 pairs for an 8-bit image), We have C(256,2)\*C(254,2)\*....\*C(2,2) = 256!/2^256  = 7.408E+429  
Total possible combinations ≈ 10^434  = 2^1441, That is 1441 bits (which is quie strong).  

##Using single layered Grayscale Image
###Input Image (Grayscale Lena)  
![Input grayscale image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/gray_lena.png)  
###Encrypted Image
![Encrypted grayscale image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/encrypted_gray_lena.png)  
###Unencypted Image  
![Unencrypted gray image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/unencrypted_gray_lena.png)  

##Using 3 layer RGB Color Image  
###Input Image (Color Lena)  
![Input color image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/color_lena.png)  
###Encrypted Image  
![Encrypted colored image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/encrypted_color_lena.png)  
###Unencrypted Image  
![Unencrypted colored image](https://raw.githubusercontent.com/27himanshu/image-enigma/master/examples/unencrypted_color_lena.png)  
