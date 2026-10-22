
#################### Program 1###########################################
# user_name="Asif"
# password="asif123"
# user=input("Enter Username:")
# user_password=input("Enter Password:")
# if user_name==user and password==user_password:
#     print("Login Successful")
# else:
#     print("Username/Password is Incorrect")

#################### Program 2 ###########################################
# import hashlib
# def hash_auth():
#     stored_password="asif123"
#     hashed_pasword=hashlib.sha256(stored_password.encode()).hexdigest()
#     print(hashed_pasword)
#     user_password=input("Enter password:")
#     user_hashed_pasword=hashlib.sha256(user_password.encode()).hexdigest()
#     if hashed_pasword==user_hashed_pasword:
#         print("Access Granted")
#     else:
#         print("Access Denied")
# hash_auth()

#################### Program 3 ###########################################
# import hashlib
# def hash_password(password):
#     """Hash a password using SHA-256."""
#     return hashlib.sha256(password.encode()).hexdigest()
# def authenticate(username, provided_password):
#     # Simulated database: usernames mapped to hashed passwords
#     user_db = {
#         "alice": hash_password("SecurePass123"),
#         "admin": hash_password("AdminP@ss!")
#     }
#     hashed_input = hash_password(provided_password)
#     if username in user_db and user_db[username] == hashed_input:
#         return "Authentication successful"
#     return "Invalid username or password"
# # Test authentication
# print(authenticate("alice", "SecurePass123"))  # Valid
# print(authenticate("alice", "wrongpassword"))

####################  Program 4 ###########################################
# import uuid
# token_store = {}  # Simulates server-side token storage
# def login(username, password):
#     """Authenticate user and issue a session token."""
#     credentials = {"admin": "SecureP@ss"}
#     if credentials.get(username) == password:
#         token = str(uuid.uuid4())
#         token_store[username] = token
#         return token  # Token issued to client
#     return None
# def access_resource(username, token):
#     """Verify token before granting resource access."""
#     if token_store.get(username) == token:
#         return "Access granted to protected resource"
#     return "Access denied: invalid or missing token"
# # Simulate authenticated access
# token = login("admin", "SecureP@ss")
# print(access_resource("admin", token))  # Valid token
# print(access_resource("admin", "fake-token"))  # Tampered token
####################  Program 5 ###########################################
# import uuid
# # Central session store — simulates the identity provider (IdP)
# sso_sessions = {}
# def sso_login(username, password):

#     """Authenticate once; issue an SSO session token."""
#     user_db = {"alice": "P@ssword1", "bob": "P@ssword2"}
#     if user_db.get(username) == password:
#         session_token = str(uuid.uuid4())
#         sso_sessions[session_token] = username
#         return session_token
#     return None
# def access_service(service_name, token):
#     """Any service validates the shared SSO token — no separate login."""
#     user = sso_sessions.get(token)
#     if user:
#         return f"{user} accessed {service_name} via SSO"
#     return "Access denied: authentication required"
#     # Single login — multiple service access
# token = sso_login("alice", "P@ssword1")
# print(access_service("Email Portal", token))
# print(access_service("HR System", token))
# print(access_service("Finance Dashboard", token))
####################  Program 6 ###########################################
# import hashlib
# def secure_login_system():
#     """Secure login: generic errors + attempt limiting."""
#     user_db = {
#         "alice": "CorrectP@ss",
#         "admin": "AdminS3cure!"
#     }
#     max_attempts = 3
#     attempts = 0
#     while attempts < max_attempts:
#         username = input("Username: ")
#         password = input("Password: ")
#         # Verify both username AND password before deciding
#         if username in user_db and user_db[username] == password:
#             print("Login successful")
#             return
#         else:
#             attempts += 1
#             remaining = max_attempts - attempts
# # SECURE: never reveal whether username or password is wrong
#         if remaining > 0:
#             print(f"Invalid username or password. {remaining} attempt(s)remaining.")
#         else:
#             print("Account temporarily locked. Contact support.")
# secure_login_system()

####################  Program 7 ###########################################
# import hashlib
# # ── auth_module.py ──────────────────────────────────────────
# USER_DB = {
#     "alice": hashlib.sha256("AliceP@ss".encode()).hexdigest(),
#     "admin": hashlib.sha256("AdminS3cure!".encode()).hexdigest()
# }
# def authenticate(username, password):
#     """Dedicated authentication function — isolated from business logic."""
#     hashed = hashlib.sha256(password.encode()).hexdigest()
#     return USER_DB.get(username) == hashed
#     # ── main_app.py ──────────────────────────────────────────────
#     # from auth_module import authenticate # Clean import in real project
# def show_dashboard(username):
#     """Business logic — contains zero authentication code."""
#     print(f"Welcome to the dashboard, {username}!")
# def main():
#     username = input("Username: ")
#     password = input("Password: ")
#     if authenticate(username, password):
#         show_dashboard(username)  # Auth concern: handled
#     else:
#         print("Invalid credentials")
# main()
######################Program  ########################################
# import random
# def otp_auth():
#     otp=random.randint(1000,9999)
#     print("OTP Gernerated:",otp)
#     user_otp=int(input("Enter OTP"))
#     if otp==user_otp:
#         print("Login Successful")
#     else:
#         print("Invalid OTP")
# otp_auth()

#################### Program 4 ###########################################
# logged_in = False

# def login():
#     global logged_in
#     password = input("Enter password: ")

#     if password == "1234":
#         logged_in = True
#         print("Login successful")
#     else:
#         print("Login failed")


# def access_resource():
#     if logged_in:
#         print("Access Granted to Secure Resource")
#     else:
#         print("Access Denied! Please login first")
# def display():
#     if logged_in:
#         print("My name is Asif")
#     else:
#         print("Access Denied! Please login first Dsiplay")

# login()
# access_resource()
# display()

#################### Program 5 ###########################################
# session = {"logged_in": False,
#            "user":"null"}
# def login():
#     user=input("Enter Username")
#     password = input("Enter password: ")
#     if password == "secure123":
#         session["logged_in"] = True
#         session["user"]=user
#         print("Login successful")
#     else:
#         print("Login failed")
# def dashboard():
#     if session["logged_in"]:
#         print("Welcome to Dashboard",session["user"])
#     else:
#         print("Access Denied")
# login()
# dashboard()

#################### Program 6 ###########################################
# import uuid
# token_store = {}
# def login():
#     user = input("Username: ")
#     pwd = input("Password: ")
#     if user == "admin" and pwd == "1234":
#         token = str(uuid.uuid4())
#         token_store[user] = token
#         print("Login successful")
#         print("Your token:", token)
#         return user, token
#     else:
#         print("Invalid credentials")
#         return None, None

#################### Program 7 ###########################################
# def access(user, token):
#     if token_store.get(user) == token:
#         print("Access Granted")
#     else:
#         print("Access Denied")


# user, token = login()

# if user:
#     access(user, token)

# def central_auth():

#     user_db = {
#         "sunil": "123",
#         "admin": "admin123",
#         "guest": "guest"
#     }

#     user = input("Enter username: ")
#     pwd = input("Enter password: ")

#     if user in user_db and user_db[user] == pwd:
#         print("Authenticated via Central System")
#     else:
#         print("Access Denied")

# central_auth()

#################### Program 8 ###########################################
# session = {"authenticated": False}

# def login():
#     user = input("Username: ")
#     pwd = input("Password: ")

#     if user == "admin" and pwd == "1234":
#         session["authenticated"] = True
#         print("Login Successful")
#     else:
#         print("Login Failed")


# def service1():
#     if session["authenticated"]:
#         print("Accessing Service 1")
#     else:
#         print("Login required")


# def service2():
#     if session["authenticated"]:
#         print("Accessing Service 2")
#     else:
#         print("Login required")


# login()
# service1()
# service2()

#################### Program 9 ###########################################
# def login_limiter():

#     user_db = {"admin": "1234"}
#     attempts = 0
#     max_attempts = 3

#     while attempts < max_attempts:

#         user = input("Username: ")
#         pwd = input("Password: ")

#         if user in user_db and user_db[user] == pwd:
#             print("Login successful")
#             return
#         else:
#             print("Invalid credentials")
#             attempts += 1

#     print("Account temporarily locked")


# login_limiter()

# auth_module.py

# main_app.py
#################### Program 10 ###########################################
# from auth_module import authenticate

# def dashboard():
#     print("Welcome to Dashboard")
# def main():
#     user = input("Username: ")
#     pwd = input("Password: ")
#     if authenticate(user, pwd):
#         dashboard()
#     else:
#         print("Access Denied")
# main()