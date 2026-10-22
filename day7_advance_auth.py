########################### Program 1 ###############################################
# import time
# import hashlib
# # Simulated database
# users = {
#     "admin": {
#         "password": hashlib.sha256("Secure123".encode()).hexdigest(),
#         "failed_attempts": 0,
#         "lock_until": 0
#     }
# }
# MAX_ATTEMPTS = 3
# LOCK_TIME = 30   # seconds


# def authenticate(username, password):
#     if username not in users:
#         return "User not found"
#     user = users[username]

#     # Check if account is locked
#     if time.time() < user["lock_until"]:
#         remaining = int(user["lock_until"] - time.time())
#         return f"Account locked. Try again in {remaining} seconds."

#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Successful login
#     if hashed_password == user["password"]:
#         user["failed_attempts"] = 0
#         return "Login successful"

#     # Failed login
#     user["failed_attempts"] += 1

#     remaining_attempts = MAX_ATTEMPTS - user["failed_attempts"]

#     if user["failed_attempts"] >= MAX_ATTEMPTS:
#         user["lock_until"] = time.time() + LOCK_TIME
#         user["failed_attempts"] = 0
#         return "Account locked due to multiple failed attempts"

#     return f"Invalid password. {remaining_attempts} attempts remaining"


# # Testing
# print(authenticate("admin", "Secure123"))
# print(authenticate("admin", "wrong"))
# print(authenticate("admin", "wrong"))
# print(authenticate("admin", "wrong"))
# print(authenticate("admin", "Secure123"))
# print(authenticate("admin", "Secure123"))
# print(authenticate("admin", "Secure123"))


# import time
# import hashlib

# MAX_ATTEMPTS = 3
# LOCK_TIME = 20  # seconds

# users = {
#     "admin": {
#         "password": hashlib.sha256("Admin123".encode()).hexdigest(),
#         "failed_attempts": 0,
#         "lock_until": 0
#     }
# }


# def login(username, password):

#     if username not in users:
#         return "Invalid username or password"

#     user = users[username]

#     # Check lockout
#     if time.time() < user["lock_until"]:
#         remaining = int(user["lock_until"] - time.time())
#         return f"Account locked. Try again after {remaining} seconds."

#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Successful login
#     if hashed_password == user["password"]:
#         user["failed_attempts"] = 0
#         return "Login Successful"

#     # Failed login
#     user["failed_attempts"] += 1

#     if user["failed_attempts"] >= MAX_ATTEMPTS:
#         user["lock_until"] = time.time() + LOCK_TIME
#         user["failed_attempts"] = 0
#         return "Account locked due to multiple failed attempts"

#     remaining = MAX_ATTEMPTS - user["failed_attempts"]

#     return f"Invalid password. Remaining attempts: {remaining}"


# # Testing
# print(login("admin", "wrong"))
# print(login("admin", "wrong"))
# print(login("admin", "wrong"))
# print(login("admin", "Admin123"))


############################ Program 2 ###############################################
# import time
# import hashlib
# users = {
#     "asif": {
#         "password": hashlib.sha256("SecurePass".encode()).hexdigest(),
#         "failed_attempts": 0
#     }
# }
# def login(username, password):

#     if username not in users:
#         return "Invalid credentials"
#     user = users[username]
#     hashed = hashlib.sha256(password.encode()).hexdigest()
#     if hashed == user["password"]:
#         user["failed_attempts"] = 0
#         return "Login successful"
#     user["failed_attempts"] += 1
#     delay = user["failed_attempts"] * 3
#     print(f"Too many failed attempts. Waiting {delay} seconds...")
#     time.sleep(delay)
#     return "Invalid password"
# # Testing
# print(login("asif", "123"))
# print(login("asif", "123"))
# print(login("asif", "123"))
# print(login("asif", "123"))
# print(login("asif", "SecurePass"))

############################ Program 3 ###############################################
# import time
# import hashlib
# LOG_FILE = "login_attempts.txt"
# users = {
#     "teacher": {
#         "password": hashlib.sha256("Teacher123".encode()).hexdigest(),
#         "attempts": 0
#     }
# }

# def log_event(message):
#     with open(LOG_FILE, "a") as file:
#         file.write(message + "\n")


# def login(username, password):

#     if username not in users:
#         log_event(f"{time.ctime()} - Invalid username attempt")
#         return "Invalid credentials"

#     user = users[username]

#     hashed = hashlib.sha256(password.encode()).hexdigest()

#     if hashed == user["password"]:
#         user["attempts"] = 0
#         log_event(f"{time.ctime()} - Successful login for {username}")
#         return "Login successful"

#     user["attempts"] += 1

#     log_event(f"{time.ctime()} - Failed login for {username}")

#     if user["attempts"] >= 3:
#         log_event(f"{time.ctime()} - Account locked for {username}")
#         return "Account locked"

#     return "Wrong password"

# # Test
# print(login("teacher", "Teacher123"))
# print(login("Asif", "wrong"))
# print(login("teacher", "wrong"))
# print(login("teacher", "wrong"))

############################ Program 4 ###############################################
# import random
# import hashlib

# users = {
#     "admin": hashlib.sha256("Admin@123".encode()).hexdigest()
# }

# failed_attempts = 0

# def captcha():
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)

#     answer = int(input(f"Solve CAPTCHA: {a} + {b} = "))

#     return answer == (a + b)


# def login():

#     global failed_attempts

#     username = input("Username: ")
#     password = input("Password: ")

#     hashed = hashlib.sha256(password.encode()).hexdigest()

#     if failed_attempts >= 2:
#         if not captcha():
#             return "CAPTCHA failed"

#     if username in users and users[username] == hashed:
#         failed_attempts = 0
#         return "Login successful"

#     failed_attempts += 1
#     return "Invalid credentials"

# print(login())
# print(login())
# print(login())

############################ Program 5 ###############################################
# import secrets
# import hashlib
# users = {
#     "admin@example.com": {
#         "password": hashlib.sha256("OldPass123".encode()).hexdigest(),
#         "reset_token": None
#     }
# }
# def request_reset(email):

#     if email not in users:
#         return "If account exists, reset link sent"

#     token = secrets.token_hex(16)

#     users[email]["reset_token"] = token

#     print(f"Reset Token: {token}")

#     return "Password reset token generated"


# def reset_password(email, token, new_password):

#     if email not in users:
#         return "Invalid request"

#     if users[email]["reset_token"] != token:
#         return "Invalid token"

#     hashed = hashlib.sha256(new_password.encode()).hexdigest()

#     users[email]["password"] = hashed

#     users[email]["reset_token"] = None

#     return "Password reset successful"
# # Example
# print(request_reset("admin@example.com"))
# print(users["admin@example.com"]["reset_token"])
# token = users["admin@example.com"]["reset_token"]
# print(reset_password(
#     "admin@example.com",
#     token,
#     "NewSecure123"
# ))

############################ Program 6 ###############################################
# Password reset with Expiry Time
# import secrets
# import time
# import hashlib

# users = {
#     "user@example.com": {
#         "password": hashlib.sha256("Pass123".encode()).hexdigest(),
#         "token": None,
#         "token_expiry": 0
#     }
# }

# def generate_reset(email):

#     token = secrets.token_urlsafe(32)

#     users[email]["token"] = token

#     users[email]["token_expiry"] = time.time() + 300

#     print("Reset Token:", token)


# def reset_password(email, token, new_password):

#     user = users[email]

#     if time.time() > user["token_expiry"]:
#         return "Token expired"

#     if token != user["token"]:
#         return "Invalid token"

#     user["password"] = hashlib.sha256(
#         new_password.encode()
#     ).hexdigest()

#     user["token"] = None

#     return "Password changed successfully"


# generate_reset("user@example.com")

# token = users["user@example.com"]["token"]

# print(reset_password(
#     "user@example.com",
#     token,
#     "NewPass456"
# ))

############################ Program 7 ###############################################
# OTP based password reset
# import random
# import hashlib

# users = {
#     "admin": {
#         "password": hashlib.sha256("Admin123".encode()).hexdigest(),
#         "otp": None
#     }
# }


# def send_otp(username):

#     otp = random.randint(100000, 999999)

#     users[username]["otp"] = otp

#     print(f"OTP Sent: {otp}")


# def reset_password(username, otp, new_password):

#     if users[username]["otp"] != otp:
#         return "Invalid OTP"

#     users[username]["password"] = hashlib.sha256(
#         new_password.encode()
#     ).hexdigest()

#     users[username]["otp"] = None

#     return "Password reset successful"


# send_otp("admin")

# otp = users["admin"]["otp"]

# print(reset_password(
#     "admin",
#     otp,
#     "SecureNewPass"
# ))


############################ Program 8 ###############################################
# OTP based MFA
# import random
# import hashlib

# users = {
#     "admin": {
#         "password": hashlib.sha256("Admin123".encode()).hexdigest(),
#         "otp": None
#     }
# }


# def login(username, password):

#     if username not in users:
#         return "Invalid credentials"

#     hashed = hashlib.sha256(password.encode()).hexdigest()

#     if hashed != users[username]["password"]:
#         return "Invalid credentials"

#     otp = random.randint(100000, 999999)

#     users[username]["otp"] = otp

#     print(f"OTP Sent: {otp}")

#     return "OTP verification required"


# def verify_otp(username, otp):

#     if users[username]["otp"] == otp:
#         users[username]["otp"] = None
#         return "Login successful"

#     return "Invalid OTP"

# # Testing
# print(login("admin", "Admin123"))
# otp=int(input("Enter the OTP:"))
# # otp = users["admin"]["otp"]
# print(verify_otp("admin", otp))


############################ Program 9 ###############################################
# MFA with OTP Expiration
# import random
# import hashlib
# import time
# users = {
#     "asif": {
#         "password": hashlib.sha256("Secure123".encode()).hexdigest(),
#         "otp": None,
#         "otp_expiry": 0
#     }
# }
# def login(username, password):

#     hashed = hashlib.sha256(password.encode()).hexdigest()

#     if hashed != users[username]["password"]:
#         return "Invalid credentials"

#     otp = random.randint(100000, 999999)

#     users[username]["otp"] = otp
#     users[username]["otp_expiry"] = time.time() + 60

#     print(f"OTP: {otp}")

#     return "OTP generated"


# def verify_otp(username, otp):

#     user = users[username]

#     if time.time() > user["otp_expiry"]:
#         return "OTP expired"

#     if otp != user["otp"]:
#         return "Invalid OTP"

#     user["otp"] = None

#     return "Authentication successful"

# print(login("asif", "Secure123"))
# otp = users["asif"]["otp"]
# print(verify_otp("asif", otp))


############################ Program 10 ###############################################
# Email Based MFA
# import smtplib
# import random
# otp = random.randint(100000, 999999)
# sender = "asif26@gmail.com"
# receiver = "ghss1001@gmail.com"
# message = f"Your OTP is: {otp}"

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(sender, "your_password")
# server.sendmail(sender, receiver, message)
# server.quit()
# print("OTP sent successfully")


############################ Program 11 ###############################################
# Time based
# import pyotp
# # Generate secret key
# secret = pyotp.random_base32()

# print("Secret Key:", secret)

# totp = pyotp.TOTP(secret)

# # Generate current OTP
# otp = totp.now()

# print("Current OTP:", otp)

# # Verify OTP
# print(totp.verify(otp))


############################ Program 12 ###############################################
# Changing Default password
# import hashlib
# import re
# default_password = "Admin@123"
# stored_password = hashlib.sha256(
#     default_password.encode()
# ).hexdigest()
# def strong_password(password):
#     if len(password) < 8:
#         return False
#     if not re.search(r"[A-Z]", password):
#         return False
#     if not re.search(r"[a-z]", password):
#         return False
#     if not re.search(r"\d", password):
#         return False
#     if not re.search(r"[!@#$%^&*]", password):
#         return False
#     return True
# new_password = input("Change default password: ")

# if not strong_password(new_password):
#     print("Weak password")
# elif new_password==default_password:
#     print("Default Password used")
# else:
#     stored_password = hashlib.sha256(
#         new_password.encode()
#     ).hexdigest()

#     print("Password updated securely")

############################ Program 13 ###############################################
# Detecting Default Credentials
# common_defaults = [
#     ("admin", "admin"),
#     ("root", "root"),
#     ("admin", "password"),
#     ("user", "1234")
# ]
# username = input("Enter username: ")
# password = input("Enter password: ")
# if (username, password) in common_defaults:
#     print("WARNING: Default credentials detected")
# else:
#     print("Credentials appear safer")
# DEFAULT_PASSWORD = "admin"
# current_password = input("Enter your current password: ")
# if current_password == DEFAULT_PASSWORD:
#     print("You are using the default password.")
#     new_password = input("Enter a new, strong password: ")
#     print(f"Password updated successfully. Please remember:{new_password}")
#     print("Access granted with your new password.")
# else:
#     print("Custom password detected. Access granted.")
