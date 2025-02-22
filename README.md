# Secure-Data-Hiding-In-Image-Using-Steganography-

**LSB Image Steganography**

This project implements Least Significant Bit (LSB) steganography to hide and extract secret messages in images.

**Features**

Encrypt a secret message into an image without noticeable changes.

Decrypt and retrieve the hidden message from the modified image.

Uses PNG format to avoid compression artifacts.

Secure message retrieval using a password-based authentication.

**Files**

encrypt.py: Script to embed a secret message into an image.

decrypt.py: Script to extract the hidden message from the encrypted image.

password.txt: Stores the password required for decryption.

**Requirements**

Make sure you have the following installed:

Python 3.x

OpenCV (cv2 library)

OS module (pre-installed in Python)

To install OpenCV, run:

pip install opencv-python

**How to Use**

**Encryption**

Place your image file (mypic.jpg) in the project directory.

Run the encryption script:

python encrypt.py

Enter the secret message and a passcode when prompted.

The modified image (encryptedImage.png) is created with the hidden message.

**Decryption**

Run the decryption script:

python decrypt.py

Enter the passcode to retrieve the hidden message.

If the passcode is correct, the message is displayed; otherwise, access is denied.

**Notes**

Ensure that the image used has enough pixels to store the message.

The password.txt file must be in the same directory for decryption to work.

The script stops extracting the message once it detects the ::END marker.

**Disclaimer**

This tool is for educational purposes only. Do not use it for illegal activities.



