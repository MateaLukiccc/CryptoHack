import cv2

img1 = cv2.imread(r"C:\Users\lukic\CryptoHack\XOR\flag.png")       
img2 = cv2.imread(r"C:\Users\lukic\CryptoHack\XOR\lemur.png")

secret_key = cv2.bitwise_xor(img1, img2)


cv2.imwrite(r"C:\Users\lukic\CryptoHack\XOR\secret_key.png", secret_key)
