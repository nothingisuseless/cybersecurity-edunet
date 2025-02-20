import cv2
import os
import string
import time 

def main():
    # Starting the code
    # Step 1: The receiver generates the public keys and shares the public key with the sender, 
    # so that the passcode can be encrypted with the sender's public key
    from passcode_exchange_using_public_key import key_generation, encrypt_passcode, decrypt_passcode
    from encryption import encode_image
    from decryption import decode_image

    print("1. Encryption\n2. Decryption")
    choice = input("Please enter your choice: ")
    
    if choice not in ('1', '2'):
        print("Invalid!!")
        exit(1)
    
    if choice == '1':
        
        print("You have selected encryption.....")
        
        key_generation()  # Generate public and private keys
        secret_message = input("Enter your message to be hidden: ")
        passcode = input("Enter a passcode for authentication: ")
        length_message = len(secret_message)
        passcode_length_msg = passcode + "|~|" + str(length_message)
        
        if len(passcode) == 0:
            print("Please enter a passcode!") 
            exit(1)
        else:
            encrypt_passcode(passcode_length_msg.encode())  # Encrypt the passcode

            
            image_path = input("Enter the image path: ")
            output_image_path = input("Enter the output image path: ")

            # Hide the message inside the image
            encode_image(image_path, secret_message, output_image_path)
    
    elif choice == '2':
        print("You have selected decryption.....")
        passcode = input("Enter a passcode for authentication: ")

        # Read the encrypted data from the file
        encrypted_file = input("Enter the path to the encrypted passcode file: ")
        with open(encrypted_file, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        
        # Decrypt and verify the passcode
        print(decrypt_passcode(encrypted_data))
        print(passcode)
        decrypted_data = decrypt_passcode(encrypted_data).decode()
        original_passcode = decrypted_data.split("|~|")[0]
        length_message = decrypted_data.split("|~|")[1]
        decrypt_passcode(encrypted_data)
        if passcode == original_passcode:
            print("Passcode verified successfully.")
            encrypted_image_file = input("Enter the path to the encrypted image file: ")
            hidden_text = decode_image(encrypted_image_file,int(length_message))
            print(f"Hidden text: {hidden_text}")
        else:
            print("Invalid passcode. Decryption failed.")
    
    else:
        print("Invalid choice!")

# Step 4: Placeholder for any additional steps (this can be expanded)

if __name__ == "__main__":
    main()
