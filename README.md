# Secure Data Hiding in Image using Steganography

This project allows you to securely hide messages inside images using encryption and steganography. It involves the following steps:

## Passcode Encryption : A passcode is used for authentication, and the passcode is encrypted using public-key encryption.

## Message Hiding : The secret message is hidden inside an image using steganography techniques.

## Decryption : The encrypted passcode is verified, and the hidden message is revealed from the image.


**Features**
**Encryption**: Encrypt a passcode for authentication, hide a secret message inside an image, and save the modified image.
**Decryption**: Verify the passcode, extract the hidden message from the encrypted image, and display it.

**Prerequisites**
Before you begin, ensure that you have the following installed:

Python 3.x
Required Python libraries (listed below)

**Required Python Libraries**
cv2 (OpenCV)
os
string
time

**Install the required libraries using pip:**

**bash**

pip install opencv-python

**Usage**

**Running the Program**
Clone this repository to your local machine:
**bash**

**git clone https://github.com/yourusername/passcode-encryption-image-steganography.git
cd passcode-encryption-image-steganography**

Start the program by running:

**bash**

python steganography_normal.py
The program will prompt you to choose between encryption or decryption:

1. Encryption: Encrypt a passcode, hide a message inside an image, and save the output.
2. Decryption: Decrypt an encrypted passcode, verify it, and extract the hidden message from the image.

**Step-by-Step Guide**

**1. Encryption**

**Process:**

1. The program will generate public and private keys for passcode encryption.

2. You will input a secret message and a passcode for authentication.

3. The passcode will be encrypted.

4. You will provide an image file to embed the secret message.

5. The program will save the encrypted image at your specified location.

**Algorithm for Encryption:**
The message characters are converted to their ASCII values.

The gcd (greatest common divisor) of the image dimensions is used as a pattern to encode the message into the image.

Pixels are modified according to the message's characters, and the result is saved as a new image.

**2. Decryption**

**Process:**

1. You will input the passcode.

2. You will provide the path to the encrypted passcode file.

3. The passcode will be decrypted, and its validity will be verified.

4. You will input the path to the encrypted image file.

5. The hidden message will be extracted and displayed.


Algorithm for Decryption:

The program reads the image and checks pixel values based on the gcd of the image dimensions.

It retrieves the hidden message encoded in the pixel values of the blue channel of the image.

It stops extracting characters once the message length is reached.


.
├── main.py               # Main program to run encryption and decryption
├── encryption.py         # Handles encryption operations (encode passcode and message)
├── decryption.py         # Handles decryption operations (decode passcode and message)
├── passcode_exchange_using_public_key.py  # Contains logic for key generation, passcode encryption/decryption
└── README.md             # Project documentation
