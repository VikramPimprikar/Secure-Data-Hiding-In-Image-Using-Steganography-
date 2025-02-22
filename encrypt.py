## encrypt.py
import cv2
import os
import string

def encrypt():
    img = cv2.imread("mypic.jpg")  # Replace with the correct image path
    msg = input("Enter secret message:")
    password = input("Enter a passcode:")

    msg += "::END"  # Append a stopping marker

    d = {chr(i): i for i in range(255)}

    m, n, z = 0, 0, 0
    height, width, _ = img.shape

    for char in msg:
        if n >= height or m >= width:
            print("Error: Message too long for image size!")
            return
        
        img[n, m, z] = d[char]
        
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.png", img)  # Save as PNG to avoid compression issues
    os.system("start encryptedImage.png")  # Open image on Windows

    with open("password.txt", "w") as f:
        f.write(password)

    print("Encryption complete. Image saved as 'encryptedImage.png'")

if __name__ == "__main__":
    encrypt()
