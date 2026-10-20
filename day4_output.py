######################  Program 1 #####################################
# import html
# import datetime 
# comments = []
# def add_comment():
#     user    = input("Enter username: ")
#     comment = input("Enter comment: ")
 
#     # Encode special characters before storing
#     # safe_comment=comment
#     safe_comment = html.escape(comment)
 
#     comments.append({
#         "user":    user,
#         "comment": safe_comment,
#         "time":    datetime.datetime.now()
#     })
#     print("Comment stored securely.")
 
# def display_comments():
#     print("\n--- All Comments ---")
#     for c in comments:
#         print(f"[{c['time']}] {c['user']}: {c['comment']}")
# while True:
#     print("\n1. Add Comment  2. View Comments  3. Exit")
#     choice = input("Choose: ")
#     if choice == "1":
#         add_comment()
#     elif choice == "2":
#         display_comments()
#     else:
#         break

#Inputs
# <script > alert(1) < /script >
# <script>alert("Hacked")</script>
########################## Program 2##########################################
# import html
# search = input("Search: ")
# # safe_search = html.escape(search)
# safe_search=search
# html_page = f"""
# <html>
#   <body>
#     <h2>Results for: {safe_search}</h2>
#   </body>
# </html>
# """
# print(html_page)

#Inputs
# Python, Hello World, < h1 > Welcome < /h1 > , < script > alert('Hacked') < /script > , < img src = x onerror = alert('XSS') > , Tom & Jerry, 5 > 3 and 2 < 4, "Programming", 'Programming', < b > Asif Farooq < /b > , < iframe src = "https://example.com" > </iframe > , < a href = "https://google.com" > Google < /a > , < svg onload = alert('XSS') > , < marquee > Hello < /marquee > , < div style = "color:red" > Red Text < /div >
######################### Program 3 #################################
# import html
# log = input("Enter log data: ")
# safe_log = html.escape(log)

# with open("secure_log.txt", "a") as f:
#     f.write(safe_log + "\n")

# print("Log saved securely.")

#################### Program 4  ####################################
# user_input="Asif"
# password=1234
# response = "{user: " + user_input + {password} "}"
# print(response)
# If user_input = 'Sunil, role: "admin"'
# Result: {user: Sunil, role: "admin"}  ← Invalid JSON
# import json
# user_name=input("Enter name")
# user_role=input("Enter role")
# user_profile=input("Enter User Profile")
# data={
#     "name":user_name,
#     "role":user_role,
#     "user_profile":user_profile
# }
# print(data)
# print(type(data))
# result=json.dumps(data)
# print(result)
# print(type(result))
############################# Program 5 #############################

# import datetime
# import json
# def generate_response():
#     user = input("Enter username: ")
#     role = input("Enter role: ")
 
#     data = {
#         "user":      user,
#         "role":      role,
#         "timestamp": str(datetime.datetime.now())
#     }
 
#     # json.dumps() handles all encoding automatically
#     print(data)
#     safe_json = json.dumps(data, ensure_ascii=False)
 
#     print("\n--- API RESPONSE ---")
#     print(safe_json)
 
# generate_response()

######################### Program 6 ###############################
# from urllib.parse import urlencode
# def generate_url():
#     base_url = "https://example.com/search"
 
#     query = {
#         "q":    input("Enter search keyword: "),
#         "page": "1"
#     }
#     safe_url = base_url + '?' + urlencode(query)
#     print("\nSafe URL:")
#     print(safe_url)
# generate_url()
# Space + ( or %20) Spaces break URL structure
# & % 26 & is a query string delimiter
# = % 3D = separates key from value
# %23 # is a fragment identifie

######################### Program 7 #################################
# import base64
# def encode_data():
#     data = input("Enter data to encode: ")
 
#     # Encode string to bytes, then Base64-encode
#     encoded = base64.b64encode(data.encode()).decode()
 
#     print("\nBase64 Encoded Output:")
#     print(encoded)
 
#     # Show how to decode it back
#     decoded = base64.b64decode(encoded).decode()
#     print("\nDecoded back to:")
#     print(decoded)
 
# encode_data()

#Inputs
# Hello World, Python123, Asif Farooq, password123, admin@123, Codingal, Hello@2026!, <script>alert('XSS')</script>, user@example.com, 9876543210, This is a secret message., I love Python 🐍, Hello & Welcome, Base64 Encoding Test, !@#$%^&*()_+-=[]{}|;':",./<>?
############################ Program 8#####################################

# import html
# import datetime
 
# def html_encoder():
#     user_input = input("Enter HTML content: ")
 
#     # quote=True also encodes single and double quotes
#     encoded = html.escape(user_input, quote=True)
 
#     print("\n--- Encoded Output ---")
#     print(encoded)
#     print("\nTimestamp:", datetime.datetime.now())
 
# html_encoder()
# <b onclick = "hack()" > Click < /b >
# <script > alert("XSS") < /script >

############################ Program 9 ############################
# from urllib.parse import quote_plus
# import datetime
 
# def url_encoder():
#     keyword = input("Enter search keyword: ")
 
#     # Encodes spaces as + and special characters as %XX
#     encoded = quote_plus(keyword)
 
#     print("\nEncoded Keyword:")
#     print(encoded)
#     print("\nGenerated at:", datetime.datetime.now())
 
# url_encoder()
#<,>,&."",'
######################### Program 10 ################################
# import html
# import datetime
 
# def render_page():
#     username = input("Enter username: ")
 
#     # HTML context — use html.escape()
#     safe_username = html.escape(username)
 
#     html_page = f"""
#     <html>
#       <body>
#         <h1>Welcome, {safe_username}</h1>
#       </body>
#     </html>
#     """
 
#     print("\n--- Rendered Page ---")
#     print(html_page)
#     print("\nGenerated at:", datetime.datetime.now())
 
# render_page()
############################# Program 11 ##################################
# import sqlite3
# import datetime
 
# def safe_query():
#     conn   = sqlite3.connect(':memory:')
#     cursor = conn.cursor()
 
#     # Create a sample users table
#     cursor.execute('CREATE TABLE users (id INTEGER, username TEXT)')
#     cursor.execute("INSERT INTO users VALUES (1, 'sunil')")
#     cursor.execute("INSERT INTO users VALUES (2, 'admin')")
 
#     username = input("Enter username to search: ")
# # SAFE: The ? placeholder separates data from SQL code
#     cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
#     result = cursor.fetchall()
#     print("\nQuery Result:", result)
#     print("Executed at:", datetime.datetime.now())
#     conn.close()
 
# safe_query()
# ' OR '1'='1
# admin' --

###################### Program 12 ##################################
# Lightweight Directory Access Protocol
# import datetime
# def ldap_escape(value):
#     # Map special characters to LDAP escape sequences
#     escape_map = {
#         "\\": "\\5c",   # Backslash must be first
#         "*":    "\\2a",
#         "(" :   "\\28",
#         ")" :   "\\29",
#         "\x00": "\\00"   # Null byte
#     }
#     return "".join(escape_map.get(c, c) for c in value)
 
# def ldap_query():
#     username      = input("Enter username: ")
#     safe_username = ldap_escape(username)
#     query         = f"(uid={safe_username})"
 
#     print("\nSafe LDAP Query:")
#     print(query)
#     print("\nGenerated at:", datetime.datetime.now())
 
# ldap_query()
# asif
# *
# *)(uid=*)
# admin)(|(uid=*)

########################### Program 13 #######################################
import subprocess
import ipaddress
import datetime
 
def safe_ping():
    target = input("Enter IP address: ")
 
    try:
        # Validate: raises ValueError if not a valid IP
        ipaddress.ip_address(target)
 
        # SAFE: list format — no shell metacharacter interpretation
# The subprocess module allows Python to start new processes, run system commands, and interact with their input and output.
# "ping" → Runs the operating system's ping command.
# "-c" → Means "count" (how many ping packets to send).
# "2" → Send only 2 ping requests.
# target → The website or IP address entered by the user.
        result = subprocess.run(
            ["ping", "-c", "2", target],
            capture_output=True,
            text=True
        )
 
        print("\n--- Ping Result ---")
        print(result.stdout)
        print("Executed at:", datetime.datetime.now())
 
    except ValueError:
        print("Error: Invalid IP address format. Input rejected.")
 
safe_ping()
# abc
# hello
# 123
# 999.999.999.999
# 256.256.256.256
# 192.168.1
# 192.168.1.1.1
# 192.168..1
# 192.168.1.-1
# 192.168.1.abc

# 8.8.8.8; ls
# 127.0.0.1 && whoami
# 8.8.8.8 | cat /etc/passwd
# 8.8.8.8; rm -rf /
# $(whoami)
# `whoami`
########################## Program 14 ###################################
# from pathlib import Path
# import datetime

# def safe_file_lookup():
#     # Define and create the safe base directory
#     BASE_DIR = Path("safe_files").resolve()
#     BASE_DIR.mkdir(exist_ok=True)

#     filename = input("Enter filename: ").strip()

#     # Resolve the full absolute path of the requested file
#     target = (BASE_DIR / filename).resolve()

#     # 🔐 CRITICAL CHECK: ensure target is inside BASE_DIR
#     try:
#         target.relative_to(BASE_DIR)   # safest check
#         if target.exists() and target.is_file():
#             print("File found:", target.name)
#         else:
#             print("File not found in safe directory.")
#     except ValueError:
#         print("ACCESS DENIED: Path traversal attempt blocked.")

#     print("Checked at:", datetime.datetime.now())

# # Run the function
# safe_file_lookup()
# ../secret.txt
# ../../etc/passwd
# ../../../home/user/data.txt

############################# Program 15 ######################################
# import subprocess
# import datetime
 
# def safe_executor():
#     # Whitelist: map safe keywords to exact command arrays
#     # allowed_commands = {
#     #     "date":   ["date"],
#     #     "disk":   ["df", "-h"],
#     #     "memory": ["free", "-h"],
#     #     "uptime": ["uptime"]
#     # }
#     allowed_commands = {
#     "date":   ["cmd", "/c", "date /t"],
#     "disk":   ["cmd", "/c", "dir"],
#     "memory": ["cmd", "/c", "systeminfo"],
#     "uptime": ["cmd", "/c", "net stats workstation"]
# }

 
#     print("Allowed commands:", ", ".join(allowed_commands.keys()))
#     choice = input("Enter command: ")
 
#     if choice in allowed_commands:
#         result = subprocess.run(
#             allowed_commands[choice],
#             capture_output=True,
#             text=True
#         )
#         print("\n--- Output ---")
#         print(result.stdout)
#     else:
#         print("Command not permitted.")
 
#     print("Executed at:", datetime.datetime.now())
 
# safe_executor()
