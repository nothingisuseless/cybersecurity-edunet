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
- `pycryptodome` (for key generations)

You can install the required dependencies using `pip`:

```bash
pip install opencv-python pycryptodome

```

### Usage


#### Running the Program

1. **Clone this repository to your local machine:**

```bash
git clone https://github.com/yourusername/secure-data-hiding-in-image-using-steganography.git

cd secure-data-hiding-in-image-using-steganography
```

2. **Run the main program using python:**

```bash
python steganography_normal.py
```
