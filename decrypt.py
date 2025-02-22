## decrypt.py
import cv2
import os

def decrypt():
    img = cv2.imread("encryptedImage.png")  # Read PNG to prevent compression artifacts
    if img is None:
        print("Error: Encrypted image not found!")
        return
    
    with open("password.txt", "r") as f:
        saved_password = f.read().strip()
    
    pas = input("Enter passcode for Decryption:")
    if pas != saved_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    c = {i: chr(i) for i in range(255)}
    
    message = ""
    m, n, z = 0, 0, 0
    height, width, _ = img.shape  # Get image dimensions

    while n < height and m < width:
        pixel_value = img[n, m, z]  # Extract pixel value
        
        char = c.get(pixel_value, '?')  # Use '?' if pixel_value is not in range
        
        if message.endswith("::END"):  # Stop at the end marker
            message = message[:-5]  # Remove marker before printing
            break
        
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decryption message:", message)

if __name__ == "__main__":
    decrypt()
