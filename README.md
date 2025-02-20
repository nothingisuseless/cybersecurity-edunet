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

## Usage


#### Running the Program

1. **Clone this repository to your local machine without GUI:**

```bash
git clone https://github.com/nothingisuseless/cybersecurity-edunet.git

cd cybersecurity-edunet/without_GUI/
```

2. **Run the main program using python without GUI:**

```bash
python steganography_normal.py
```

3. **For Running with GUI**

```bash
git clone https://github.com/nothingisuseless/cybersecurity-edunet.git

cd cybersecurity-edunet/GUI/
```

4. **Run the encryption script first using streamlit**

```bash
streamlit run encryption.py
```

5. **For decryption, add the passcode.txt file and private and public keys to the same folder then run**

```bash
streamlit run decryption.py
```


## Step by step process

1. Public and Private key generation

2. Receiver sends their private key to the sender

3. Sender generates the passcode while encoding process and encrypts it with public key of the receiver and then encodes it in image

4. Sender sends the image and the encrypted passcode file to receiver which can be only opened using private key of receiver

5. Once the sender enters the correct passcode, the hidden text is visible
