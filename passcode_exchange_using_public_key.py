def key_generation():
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

	print("RSA public and private keys generated and saved to files.")
	

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
	with open(r"D:\Education\Cyber Security\IBM\Edunet\Final\encrypted_passcode.txt", "wb") as encrypted_file:
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


