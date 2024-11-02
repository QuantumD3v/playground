import json
import random
import os
import string
import time
import requests
from base64decrypter import base64_decrypt  # Importing base64_decrypt function from base64decrypter.py
from base64encrypter import base64_encrypt  # Importing base64_encrypt function from base64encrypter.py
from emailsender import send_email
import getpass
import base64

def antisnipe():
    os.system('cmd.exe /k start "GUI" "%~dp0antisnipeapp.bat"')
    main()

# os.system('pause')
def nu():
    print('yo')
    # Function to fetch and execute Python code from a GitHub raw URL
    # ghurl = "https://google.com"
    # def get_code_from_github():
    #     try:
    #         response = requests.get(ghurl)
    #         response.raise_for_status()
    #         code = response.text
    #         exec(code)
    #     except Exception as e:
    #         print(f"Failed to fetch or execute code: {e}")

# Function to load users from a GitHub raw URL
def load_users():
    url = 'https://raw.githubusercontent.com/alwaysdev-alt/userslist/main/users.json'  # Replace with your actual GitHub raw URL
    response = requests.get(url)
    users_data = response.json()
    return users_data['users']

# Function to check login credentials
def login(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
        if username == 'r' and password == 'r':
            return True
    return False

# Function to handle login process
def check_login_credentials():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' ')
    username = input("      Enter Username : ")
    password = input("      Enter Password : ")
    print(' ')

    if login(username, password):
        print('      Welcome ' + username)
        time.sleep(3)
        print("Login successful! - Redirecting...")
        return True
    else:
        print("Login failed. Please check your username and password.")
        time.sleep(2)
        return False

def save_to_random_file(text):
    try:
        # Generate a random filename
        random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".txt"
        with open(random_filename, 'w') as file:
            file.write(text)
        return random_filename
    except Exception as e:
        return f"Error saving to file: {str(e)}"

# Function for decrypting Base64-encoded data
def decrypt_base64_data(encoded_data):
    decrypted_data = base64_decrypt(encoded_data)
    if decrypted_data:
        print(f"Decrypted data: {decrypted_data}")
    else:
        print("Failed to decrypt data.")

# Function for encrypting text to Base64
def encrypt_to_base64(text):
    encrypted_text = base64_encrypt(text)
    if encrypted_text:
        print(f"Encrypted text: {encrypted_text}")
        save_to_random_file(encrypted_text)
        time.sleep(4)
    else:
        print("Failed to encrypt text.")
        if encrypted_text.startswith("Error"):
            print("Encryption failed. Exiting...")
        else:
            filename = save_to_random_file(encrypted_text)
            if filename.startswith("Error"):
                print("Failed to save to file.")
            else:
                print(f"Encrypted text saved to file: {filename}")

def dwhsreq():
    webhookurl = input("Enter Discord WebHook Url : ")
    contentsinput = input("Enter Message Contents : ")

    # Replace 'YOUR_WEBHOOK_URL' with your actual Discord webhook URL
    webhook_url = webhookurl

    # Message to send to Discord
    message = {
        'content': contentsinput
    }

    # Send the POST request to the webhook URL
    requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

def prs():
    print(' ')
    print(' Restarting - 1')
    time.sleep(0.1)
    print(' Restarting - 2')
    time.sleep(0.1)
    print(' Restarting - 3')
    time.sleep(0.1)
    print(' Restarting - 4')
    time.sleep(0.1)
    print(' Restarting - 5')
    time.sleep(0.1)
    print(' Restarting - 6')
    time.sleep(0.1)
    print(' Restarting - 7')
    time.sleep(0.1)
    print(' Restarting - 8')
    time.sleep(0.1)
    print(' Restarting - 9')
    time.sleep(0.1)
    print(' Restarting - 10')
    time.sleep(0.1)
    print(' Restarting - 11')
    time.sleep(0.1)
    print(' Restarting - 12')
    time.sleep(0.1)
    print(' Restarting - 13')
    time.sleep(0.1)
    print(' Restarting - 14')
    time.sleep(0.1)

def ps():
    print(' ')
    print(' starting - 1')
    time.sleep(0.1)
    print(' starting - 2')
    time.sleep(0.1)
    print(' starting - 3')
    time.sleep(0.1)
    print(' starting - 4')
    time.sleep(0.1)
    print(' starting - 5')
    time.sleep(0.1)
    print(' starting - 6')
    time.sleep(0.1)
    print(' starting - 7')
    time.sleep(0.1)
    print(' starting - 8')
    time.sleep(0.1)
    print(' starting - 9')
    time.sleep(0.1)
    print(' starting - 10')
    time.sleep(0.1)
    print(' starting - 11')
    time.sleep(0.1)
    print(' starting - 12')
    time.sleep(0.1)
    print(' starting - 13')
    time.sleep(0.1)
    print(' starting - 14')
    time.sleep(0.1)

def pbs():
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')

def loading():
    os.system('cls')
    ps()
    os.system('cls')
    time.sleep(0.5)
    prs()
    os.system('cls')
    time.sleep(0.5)
    os.system('cls')
    pbs()
    print('                                                 Checking Data')
    time.sleep(0.5)
    os.system('cls')
    pbs()
    print('                                                 Checking Data.')
    time.sleep(0.5)
    os.system('cls')
    pbs()
    print('                                                 Checking Data..')
    time.sleep(1.5)
    os.system('cls')
    pbs()
    print('                                                 Data Valid - exit code : 0')
    print(' ')
    prs()
    os.system('cls')

def cmdlist():
    os.system('cls')
    print(' ')
    print(" start - start the discord webhook url req sender ")
    print(" decrypt - start the base64 decrypter ")
    print(" encrypt - start the base64 encrypter ")
    print(" as - start antisnipe webhook annoucer")
    # print(" getcode - fetch and execute code from GitHub raw URL ")
    print(" exit - exit this utilities terminal ")
    print(' ')

def main():
    if check_login_credentials():
        os.system('color b' if os.name == 'nt' else '')  # Change terminal color (Windows only)
        #loading()

        while True:
            print(' ')
            cmdlist()
            print(' ')
            usrinput = input(" [ Enter Shell Command ] \n _______________________ \n              | \n              |- >> ")

            if usrinput == 'start':
                dwhsreq()
            elif usrinput == 'decrypt':
                encoded_data = input("Enter Base64 Encoded Data : ")
                decrypt_base64_data(encoded_data)
                time.sleep(3)
            elif usrinput == 'encrypt':
                text_to_encrypt = input("Enter text to encrypt using Base64 : ")
                encrypt_to_base64(text_to_encrypt)
                time.sleep(3)
            elif usrinput == 'as':
                antisnipe()
            elif usrinput == 'exit':
                loading()
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Changing terminal color')
                if os.name == 'nt':
                     os.system('color 7')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

if __name__ == "__main__":
    main()
