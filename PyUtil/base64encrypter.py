import base64
import string
import random
import os

#

folderpath = 'base64/encrypt_outputs'

def randomnumber():
    random.randint(1000,100000)

def save_to_random_file(text):
    try:
        # Generate a random filename
        random_filename = os.path.join(folderpath, 'base64_encrypt_output_' + ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".txt")
        with open(random_filename, 'w') as file:
            file.write(text)
        return random_filename
    except Exception as e:
        return f"Error saving to file: {str(e)}"

def base64_encrypt(text):
    try:
        # Encode the text to bytes
        encoded_bytes = text.encode('utf-8')
        # Perform Base64 encoding
        encoded_text = base64.b64encode(encoded_bytes).decode('utf-8')
        save_to_random_file(encoded_text)
        print(save_to_random_file)
        return encoded_text
    except Exception as e:
        return f"Error encoding to base64: {str(e)}"

# Example usage:
if __name__ == "__main__":
    text_to_encrypt = input("Enter text to encrypt using Base64: ")
    encrypted_text = base64_encrypt(text_to_encrypt)
    print(f"Encrypted text: {encrypted_text}")
