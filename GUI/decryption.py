import cv2
import streamlit as st
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Decrypt the password with the private key
def decrypt_passcode(encrypted_data):
    # Load the private key
    with open("private_key.pem", "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())

    # Decrypt the data
    cipher = PKCS1_OAEP.new(private_key)
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode()
    except ValueError:
        print("Decryption failed. Possible issues with the encrypted data or key mismatch.")
        return None

# Streamlit App
def app():
    st.title("Image Decoder")

    # File uploader to upload an image
    uploaded_file = st.file_uploader("Choose the encoded image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        passcode = st.text_input("Enter a passcode for authentication: ")

        # File uploader for the encrypted passcode
        encrypted_file = st.file_uploader("Upload the encrypted passcode file", type=["txt"])

        if encrypted_file:
            # Read the content of the uploaded encrypted passcode file as bytes
            encrypted_data = encrypted_file.read()

            # Decrypt the passcode
            decrypted_data = decrypt_passcode(encrypted_data)
            if decrypted_data:
                original_passcode, length_message = decrypted_data.split("|~|")

                # Check if the entered passcode matches the original
                if passcode == original_passcode:
                    st.success("Passcode verified successfully.")
                    

                    if uploaded_file:
                        hidden_text = decode_image(uploaded_file.read(), int(length_message))  # Pass the file content as bytes
                        st.write(f"Hidden text: {hidden_text}")
                else:
                    st.error("Invalid passcode. Decryption failed.")
            else:
                st.error("Decryption failed.")

def decode_image(img_loc, message_length):
    # Decode the image and extract hidden message
    img = get_image(img_loc)
    pattern = gcd(len(img), len(img[0]))
    message = ''
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i - 1 * j - 1) % pattern == 0:
                if img[i - 1][j - 1][0] != 0:
                    message = message + chr(img[i - 1][j - 1][0])
                else:
                    if message_length == len(message):
                        return message
                    else:
                        return "Error: Message length mismatch."

# Helper functions to extract and process the image
def get_image(image_location):
    # Convert the uploaded image (bytes) to a NumPy array
    img = cv2.imdecode(np.frombuffer(image_location, np.uint8), cv2.IMREAD_COLOR)
    return img

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

if __name__ == "__main__":
    app()
