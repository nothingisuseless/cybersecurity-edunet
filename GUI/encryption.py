import cv2
import streamlit as st
import numpy as np
from io import BytesIO
import time

def key_generation():
    # Check if keys are already generated (using session state)
    if 'keys_generated' not in st.session_state:
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes

        # Generate RSA key pair
        key = RSA.generate(2048)

        # Export private key
        private_key = key.export_key()
        with open("private_key.pem", "wb") as private_file:
            private_file.write(private_key)

        # Export public key
        public_key = key.publickey().export_key()
        with open("public_key.pem", "wb") as public_file:
            public_file.write(public_key)

        # Mark keys as generated in session state
        st.session_state.keys_generated = True

        # This print will only happen once when keys are first generated
        print("RSA public and private keys generated and saved to files.")
    else:
        # This print will not happen in subsequent reruns because the session state is tracking it
        pass


## Generate the password and encrypt the password with public key
def encrypt_passcode(password):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import os

    # Load the public key
    with open("public_key.pem", "rb") as pub_file:
        public_key = RSA.import_key(pub_file.read())

    # Encrypt the file using the public key
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(password)

    # Write the encrypted data to a file
    with open(r"encrypted_passcode.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_passcode(encrypted_data):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP

    # Load the private key
    with open("private_key.pem", "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())

    # Decrypt the data using the private key
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher.decrypt(encrypted_data)

    return decrypted_data


def char_generator(message):
    for c in message:
        yield ord(c)


def get_image(image_location):
    img = cv2.imdecode(np.frombuffer(image_location, np.uint8), cv2.IMREAD_COLOR)
    return img


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def encode_image(image_location, msg, output_image_path):
    img = get_image(image_location)
    msg_gen = char_generator(msg)
    pattern = gcd(len(img), len(img[0]))
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i + 1 * j + 1) % pattern == 0:
                try:
                    img[i - 1][j - 1][0] = next(msg_gen)
                except StopIteration:
                    img[i - 1][j - 1][0] = 0
                    # Save the encoded image
                    cv2.imwrite(output_image_path, img)
                    return output_image_path  # return the output image path


# Streamlit App
def app():
    st.title("Image Encoder")

    # File uploader to upload an image
    uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Get the message input
        secret_message = st.text_input("Enter Message to Encode:")

        passcode = st.text_input("Enter a passcode for authentication: ")

        length_message = len(secret_message)
        passcode_length_msg = passcode + "|~|" + str(length_message)
            
        if len(passcode) == 0:
            print("Please enter a passcode!") 
            exit(1)
        else:
            encrypt_passcode(passcode_length_msg.encode())  # Encrypt the passcode

        # Get the output path input
        output_image_path = st.text_input("Output Image Path (with extension):", value="encoded_image.png")

        if st.button("Encode Image"):
            # Check if the message and output path are provided
            if not secret_message or not output_image_path:
                st.error("Please fill all the fields (Message, Output Path).")
            else:
                try:
                    # Encode the image
                    result = encode_image(uploaded_file.getvalue(), secret_message, output_image_path)
                    st.success(f"Image with encoded message saved as {result}")
                    st.image(result, caption="Encoded Image", use_container_width=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    # Call key_generation only if keys have not been generated before
    key_generation()

    app()
