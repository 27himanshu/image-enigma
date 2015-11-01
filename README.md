# image-enigma


Using Enigma machine to encrypt images.  

For an 8-bit image and 2 rotors we have 2\*255\*255=130050 combinations  
Assuming fixed reflectros, that is wiring of reflector cannot be changed.  
Using a maximum possible pairs of plugboard wires (128 pairs for an 8-bit image), We have (<sup>256</sup>C<sub>2</sub> \* <sup>254</sup>C<sub>2</sub> \* .... \* <sup>2</sup>C<sub>2</sub>)/123! = 256!/(2<sup>256</sup> * 123!)  = 6.099E+224  
Total possible combinations ≈ 10<sup>229</sup>  = 2<sup>768</sup>, That is 768 bits.  

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
