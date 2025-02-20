import cv2
import streamlit as st
import numpy as np
from io import BytesIO

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
        message = st.text_input("Enter Message to Encode:")

        # Get the output path input
        output_image_path = st.text_input("Output Image Path (with extension):", value="encoded_image.png")

        if st.button("Encode Image"):
            # Check if the message and output path are provided
            if not message or not output_image_path:
                st.error("Please fill all the fields (Message, Output Path).")
            else:
                try:
                    # Encode the image
                    result = encode_image(uploaded_file.getvalue(), message, output_image_path)
                    st.success(f"Image with encoded message saved as {result}")
                    st.image(result, caption="Encoded Image", use_container_width=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
