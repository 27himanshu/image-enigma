# image-enigma


Using Enigma machine to encrypt images.  
For an 8-bit image and 2 rotors we have 2\*255\*255=130050 combinations  
With 10 pairs of plugboard wires we have C(255,2)\*C(253,2)\*C(251,2)...\*C(235,2) = 144,344,660,914,893,408,208,528,832,440,536,336,416,008,344,832 possible combinations.  
In total (with 10 pairs of plugboard wires and 2 rotors) there are 1.877202315198188773752E+52 combinations for initial setup of rotors and plugboard.   
However with only 10 pairs of plugboard wires we cannot generate enough entropy (or randomness) to completely encrypt the image, therefore in this project I've used the maximum possible pairs of plugboard for an 8 bit image i.e. 256/2=128 pairs.  
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
