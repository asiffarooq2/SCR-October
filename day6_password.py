################### Program 1 ##############################
# import hashlib
# def hash_password():
#     password1 = input("Enter password: ")
#     password2 = input("Enter password: ")
#     hashed1 = hashlib.sha256(password1.encode()).hexdigest()
#     hashed2 = hashlib.sha256(password2.encode()).hexdigest()
#     print("Hashed Password:")
#     print(hashed1)
#     print(hashed2)
# hash_password()

################### Program 2 ##############################
# import hashlib
# import os
# def salted_hash():
#     password = input("Enter password: ")
#     salt = os.urandom(16)   # 16 random bytes
#     hashed_new = hashlib.sha256(password.encode()).hexdigest()
#     hashed = hashlib.sha256(salt + password.encode()).hexdigest()
#     print("Hashed form:  ",hashed_new)
#     print("Salt:       ", salt.hex())
#     print("Salted Hash:", hashed)
# salted_hash()

# ################### Program 3 ##############################
# import hashlib
# import os
# # Simulate registration — hash and store the password
# password = "secure123"
# salt = os.urandom(16)
# stored_hash = hashlib.sha256(
#     salt + password.encode()
# ).hexdigest()

# def verify():
#     user_input = input("Enter password: ")
#     check_hash = hashlib.sha256(
#         salt+ user_input.encode()
#     ).hexdigest()
#     if check_hash == stored_hash:
#         print("Password Verified — Access Granted")
#     else:
#         print("Invalid Password — Access Denied")
# verify()

# ################### Program 4 ##############################
# # password = input("Enter password: ")
# # if len(password) >= 8:
# #     print("Acceptable length — minimum requirement met")
# # else:
# #     print("Password too short — minimum 8 characters required")

# ################### Program 6 ##############################
# import re
# password = input("Enter password: ")
# if (re.search(r"[A-Z]", password) and # At least one uppercase
#     re.search(r"[a-z]", password) and # At least one lowercase
#     re.search(r"[0-9]", password) and # At least one digit
#     re.search(r"[@$!%*?&]", password)): # At least one special character
#     print("Strong Password — all complexity requirements met")
# else:
#     print("Weak Password — one or more complexity requirements failed")

# ################### Program 7 ##############################
# import re
# def validate_password(password):
#     checks = [
#     len(password) >= 12, # Minimum 12 characters
#     bool(re.search(r"[A-Z]", password)), # At least one uppercase
#     bool(re.search(r"[a-z]", password)), # At least one lowercase
#     bool(re.search(r"[0-9]", password)), # At least one digit
#     bool(re.search(r"[@$!%*?&]", password))# At least one special char
#     ]
#     if all(checks):
#         print("Policy Passed — password meets all requirements")
#     else:
#         print("Policy Failed — password does not meet all requirements")
# validate_password(input("Enter password: "))

# ################### Program 8 ##############################
# import requests
# response = requests.get("https://google.com")
# print("Status Code:", response.status_code)
# print("Connection:", "Secure (HTTPS)")

# ################### Program 9 ##############################
# import ssl
# import socket
# hostname = "google.com"
# context = ssl.create_default_context()
# with socket.create_connection((hostname, 443)) as sock:
#     with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#         print("Host: ", hostname)
#         print("TLS Version: ", ssock.version())
#         print("Cipher: ", ssock.cipher()[0])

# ################### Program 10 ##############################
# Simulated password history
# old_passwords = ["admin123", "hello123", "pass2023"]
# new_password = input("Enter new password: ")
# if new_password in old_passwords:
#     print("Rejected — this password has been used previously.")
# else:
#     print("Accepted — password is unique and has not been used before.")


# ################### Program 11 ##############################
class PasswordManager:
    def __init__(self, history_limit=5):
        self.history = []
        self.history_limit = history_limit
        print("Constructor Called...")
    def change_password(self, new_password):
        if new_password in self.history:
            print(f"Rejected — must differ from your last {self.history_limit},passwords.")
            return False
        # Add new password and trim history to the limit
        self.history.append(new_password)
        if len(self.history) > self.history_limit:
            self.history.pop(0)
            print("Password updated successfully.")
        return True
manager = PasswordManager()
manager.change_password("Pass@2021")
manager.change_password("Pass@2022")
manager.change_password("Pass@2023") # Attempt to reuse
manager.change_password("Pass@2024")
manager.change_password("Pass@2025")
manager.change_password("Pass@2025")