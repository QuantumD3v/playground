# decrypter.py

import base64

def base64_decrypt(encoded_text):
    try:
        # Decode the base64-encoded string
        decoded_bytes = base64.b64decode(encoded_text)
        # Convert bytes to string
        decoded_text = decoded_bytes.decode('utf-8')  # Assuming utf-8 encoding
        return decoded_text
    except Exception as e:
        return f"Error decoding base64: {str(e)}"

# Example usage:
if __name__ == "__main__":
    encoded_string = input("Enter base64 encoded string to decrypt: ")
    decrypted_text = base64_decrypt(encoded_string)
    print(f"Decrypted text: {decrypted_text}")
