# Passcode Encryption and Image Steganography

This project allows you to securely hide messages inside images using encryption and steganography. It involves the following steps:

**Passcode Encryption**: A passcode is used for authentication, and the passcode is encrypted using public-key encryption.
**Message Hiding**: The secret message is hidden inside an image using steganography techniques.
**Decryption**: The encrypted passcode is verified, and the hidden message is revealed from the image.


**Features**
**Encryption**: Encrypt a passcode for authentication, hide a secret message inside an image, and save the modified image.
**Decryption**: Verify the passcode, extract the hidden message from the encrypted image, and display it.

**Prerequisites**
Before you begin, ensure that you have the following installed:

Python 3.x
Required Python libraries (listed below)
Required Python Libraries
cv2 (OpenCV)
os
string
time

**Install the required libraries using pip:**

**bash**

pip install opencv-python
Usage
Running the Program
Clone this repository to your local machine:
bash

git clone https://github.com/yourusername/passcode-encryption-image-steganography.git
cd passcode-encryption-image-steganography
Start the program by running:
bash
Copy
python main.py
The program will prompt you to choose between encryption or decryption:

1. Encryption: Encrypt a passcode, hide a message inside an image, and save the output.
2. Decryption: Decrypt an encrypted passcode, verify it, and extract the hidden message from the image.
Step-by-Step Guide
1. Encryption
When you select Encryption, the following steps will occur:
The program will generate public and private keys.
You will input a secret message to hide and a passcode for authentication.
The passcode will be encrypted.
You will provide an image file to embed the secret message.
The encrypted image will be saved at the output path you specify.
2. Decryption
When you select Decryption, the following steps will occur:
You will input a passcode.
You will provide the path to the encrypted passcode file.
The passcode will be decrypted, and its validity will be verified.
You will provide the path to the encrypted image.
The hidden message in the image will be revealed.
Example
Encryption:

yaml
Copy
1. Encryption
Enter your message to be hidden: Hello, this is a secret message!
Enter a passcode for authentication: mypasscode
Enter the image path: input_image.png
Enter the output image path: output_image.png
Decryption:

pgsql
Copy
2. Decryption
Enter a passcode for authentication: mypasscode
Enter the path to the encrypted passcode file: encrypted_passcode.bin
Enter the path to the encrypted image file: output_image.png
Project Structure
bash
Copy
.
├── main.py               # Main program to run encryption and decryption
├── encryption.py         # Handles encryption operations (encode passcode and message)
├── decryption.py         # Handles decryption operations (decode passcode and message)
├── passcode_exchange_using_public_key.py  # Contains logic for key generation, passcode encryption/decryption
└── README.md             # Project documentation
