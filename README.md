# Secure Data Hiding in Image Using Steganography

This project enables secure message hiding inside images using encryption and steganography techniques. It involves encrypting a passcode for authentication, followed by embedding a secret message inside an image. On the decryption side, it validates the passcode and extracts the hidden message.

## Features

- **Encryption**: Encrypt a passcode, hide a secret message inside an image, and save the encoded image.
- **Decryption**: Decrypt the passcode, validate it, and extract the hidden message from the image.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Required Python libraries

### Required Python Libraries

- `opencv-python` (for image manipulation)

You can install the required dependencies using `pip`:

```bash
pip install opencv-python
