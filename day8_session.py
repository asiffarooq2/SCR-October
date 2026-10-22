# Program 1: Cryptographically Secure Session Generator
# Uses Python's secrets module (CSPRNG) for token generation
# import secrets
# import time
# def generate_session(username):
# # secrets.token_hex(32) generates 32 random bytes = 64 hex characters
#     session_id = secrets.token_hex(32)
#     session = {
#     "session_id" : session_id,
#     "user" : username,
#     "created_at" : time.time(),
#     "expires_in" : "30 minutes"
#     }
#     print("[+] Secure Session Generated Successfully")
#     for key, value in session.items():
#         print(f" {key}: {value}")
#     return session
# generate_session("Asif Farooq ")

####################################################################################
# # Program 2: JWT-Style Session Token Simulation
# # Demonstrates the three-part structure: Header.Payload.Signature
# import base64
# import json
# def create_jwt_simulation(username, role):
#     # Part 1: Header specifies algorithm and token type
#     header = {"alg": "HS256", "typ": "JWT"}
#     # Part 2: Payload carries the user claims (data)
#     payload = {"user": username, "role": role, "iat": 1715200000}
#     # Encode each part in Base64URL format
#     header_enc =base64.urlsafe_b64encode(json.dumps(header).encode()).decode()
#     payload_enc =base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
#     # Part 3: In production, a cryptographic signature is appended
#     token = f"{header_enc}.{payload_enc}.<signature>"
#     print("[+] JWT-Style Token Generated:")
#     print(f" Token: {token}")
#     print(" Note: In production, use the 'PyJWT' library for verified tokens.")
# create_jwt_simulation("alice", "admin")

######################################################################################
#Hash-based Message Authentication Code
# Program 3: Session Integrity Verification
# HMAC signature ensures session data has not been tampered with
# import hashlib
# import hmac
# SECRET_KEY = b"super_secret_server_key"
# def sign_session(session_data):
#     signature = hmac.new(
#         SECRET_KEY,
#         session_data.encode(),
#         hashlib.sha256
#     ).hexdigest()

#     return signature

# def verify_session(session_data, received_signature):
#     expected = sign_session(session_data)
#     if hmac.compare_digest(expected, received_signature):
#         print("[+] Session Integrity Verified. Data is authentic.")
#     else:
#         print("[!] ALERT: Session data has been tampered with!")

# # Simulate signing a session on login
# session = "user=alice&role=admin"

# sig = sign_session(session)

# print(f"Original Session: {session}")
# print(f"Signature: {sig}")

# # Simulate verifying an unmodified session
# verify_session(session, sig)
# # Simulate an attacker modifying session data
# tampered = "user=alice&role=superadmin"
# verify_session(tampered, sig)

#################################################################################
# Program 4: Advanced Session Creation System
# Creates a full session record with security metadata
# import secrets
# import datetime
# SESSION_TIMEOUT_MINUTES = 30
# def create_session(username, ip_address, user_agent):
#     now = datetime.datetime.utcnow()
#     expiry = now + datetime.timedelta(
#         minutes=SESSION_TIMEOUT_MINUTES
#     )
#     session = {
#         "session_id": secrets.token_hex(32),
#         "username": username,
#         "ip_address": ip_address,
#         "user_agent": user_agent,
#         "created_at": str(now),
#         "expires_at": str(expiry),
#         "is_active": True
#     }
#     print("[+] Session Created Successfully:")
#     for k, v in session.items():
#         print(f" {k:15}: {v}")
#     return session
# create_session(
#     "alice",
#     "192.168.1.10",
#     "Chrome/124"
# )

###########################################################################################
# Program 5: Idle Timeout Session Manager
# Expires a session after a period of user inactivity
# import time
# import secrets
# TIMEOUT_SECONDS = 30   # In production: 15–30 minutes

# def monitor_session(session_id):
#     last_activity = time.time()
#     print(f"[+] Session {session_id[:16]}... is active.")
#     print(f" Idle timeout set to {TIMEOUT_SECONDS} seconds.")

#     while True:

#         elapsed = time.time() - last_activity

#         if elapsed >= TIMEOUT_SECONDS:
#             print(
#                 f"[!] Session expired after "
#                 f"{TIMEOUT_SECONDS}s of inactivity."
#             )
#             print(
#                 " User must re-authenticate to continue."
#             )
#             break

#         # Simulate checking for activity every 5 seconds
#         time.sleep(5)

#         print(
#             f" Session active. "
#             f"{TIMEOUT_SECONDS - elapsed:.0f}s until expiry."
#         )
# monitor_session(secrets.token_hex(16))

##############################################################################
# Program 6: Session Regeneration After Successful Login
# Prevents session fixation by issuing a new ID post-authentication
# import secrets
# def pre_login_session():
#     """
#     Represents the session that existed before the user logged in.
#     """
#     return secrets.token_hex(8)


# def regenerate_session(old_session_id, username):
#     """
#     Destroys old session and issues a fresh,
#     high-entropy session ID.
#     """

#     print(f"[~] Old pre-auth session ID : {old_session_id}")

#     print("[~] User authenticated. Regenerating session...")

#     new_session_id = secrets.token_hex(32)

#     print(f"[+] New authenticated session: {new_session_id}")

#     print(f"[+] Session bound to user : {username}")

#     return new_session_id


# # Simulate the login flow
# old_id = pre_login_session()

# new_id = regenerate_session(old_id, "alice")

###################################################################################
# Program 7: Secure Cookie Configuration
# Demonstrates all recommended security flags
# for a session cookie
# import secrets
# def create_secure_cookie(username):
#     session_id = secrets.token_hex(32)
#     cookie = {
#         "name": "session_id",
#         "value": session_id,
#         "HttpOnly": True,
#         # Blocks JavaScript access (XSS protection)
#         "Secure": True,
#         # HTTPS-only transmission
#         "SameSite": "Strict",
#         # Blocks cross-site requests (CSRF protection)
#         "Path": "/",
#         # Scope cookie to entire application
#         "Max-Age": 1800,
#         # Expires after 30 minutes (seconds)
#         "Domain": "example.com"
#     }

#     print(f"[+] Secure cookie created for user: {username}")

#     for flag, value in cookie.items():
#         print(f" {flag:12}: {value}")

#     return cookie
# create_secure_cookie("alice")



#####################################################################
# Program 8: HTTPS Enforcement Checker
# Ensures session cookies are only sent over secure connections

# def check_connection_security(url):

#     print(f"[~] Checking connection security for: {url}")
#     if url.lower().startswith("https://"):

#         print("[+] Secure HTTPS connection detected.")

#         print(" Session cookie may be transmitted safely.")

#         return True

#     else:

#         print("[!] WARNING: Insecure HTTP connection detected.")

#         print(" Session cookie transmission BLOCKED.")

#         print(
#             " Redirect user to HTTPS before issuing session."
#         )

#         return False


# # Test cases

# check_connection_security(
#     "https://bank.example.com/dashboard"
# )

# print()

# check_connection_security(
#     "http://bank.example.com/dashboard"
# )

#####################################################################################

# Program 9: Cookie Expiration and Rotation
# Short-lived cookies with automatic rotation
# reduce theft window
# import secrets
# import time
# def create_expiring_cookie(max_age_seconds=1800):
#     return {
#         "session": secrets.token_hex(32),

#         "created_at": time.time(),

#         "max_age": max_age_seconds,

#         "expires_at": time.time() + max_age_seconds
#     }

# def is_cookie_expired(cookie):

#     return time.time() > cookie["expires_at"]


# def rotate_cookie_if_needed(cookie):

#     if is_cookie_expired(cookie):

#         print("[!] Cookie expired. Issuing new session cookie.")

#         return create_expiring_cookie()

#     else:

#         remaining = cookie["expires_at"] - time.time()

#         print(
#             f"[+] Cookie valid. "
#             f"Expires in {remaining:.0f} seconds."
#         )

#         return cookie


# cookie = create_expiring_cookie(max_age_seconds=2)

# print("[+] Cookie created. Checking status...")

# rotate_cookie_if_needed(cookie)
# time.sleep(2)
# rotate_cookie_if_needed(cookie)
# print(is_cookie_expired(cookie))
# print(is_cookie_expired(cookie))
# print(is_cookie_expired(cookie))
# # is_cookie_expired(cookie)
# rotate_cookie_if_needed(cookie)

################################################################################
# Program 10: IP Address + User-Agent Session Validation
# Detects context changes that may indicate session hijacking
# def create_session(username, ip, user_agent):
#     """
#     Stores the session with the user's original network context.
#     """

#     return {
#         "username": username,
#         "ip_address": ip,
#         "user_agent": user_agent
#     }


# def validate_request(session, request_ip, request_agent):
#     """
#     Compares current request context
#     with stored session context.
#     """

#     ip_match = (
#         session["ip_address"] == request_ip
#     )

#     agent_match = (
#         session["user_agent"] == request_agent
#     )

#     if ip_match and agent_match:

#         print(
#             "[+] Session Valid: "
#             "Context matches. Request approved."
#         )

#     elif not ip_match:

#         print(
#             "[!] ALERT: IP address mismatch. "
#             "Possible session hijacking!"
#         )

#         print(
#             f" Expected: {session['ip_address']} "
#             f"Got: {request_ip}"
#         )

#     else:

#         print(
#             "[!] ALERT: User-Agent mismatch. "
#             "Possible session hijacking!"
#         )


# # Simulate a normal request

# session = create_session(
#     "alice",
#     "192.168.1.5",
#     "Chrome/124"
# )

# validate_request(
#     session,
#     "192.168.1.5",
#     "Chrome/124"
# )

# # Simulate a hijacked request
# # from a different location

# validate_request(
#     session,
#     "10.0.0.99",
#     "Firefox/115"
# )


#######################################################################################
# Program 11: Secure Logout — Complete Session Destruction
# Invalidates session both server-side and client-side on logout

# import secrets
# # Simulate the server-side session store
# SESSION_STORE = {}
# def login(username):

#     session_id = secrets.token_hex(32)

#     SESSION_STORE[session_id] = {
#         "username": username,
#         "active": True
#     }

#     print(
#         f"[+] Login successful. "
#         f"Session ID: {session_id[:16]}..."
#     )

#     return session_id


# def logout(session_id):

#     if session_id in SESSION_STORE:

#         user = SESSION_STORE[session_id]["username"]

#         # Remove from server-side store
#         del SESSION_STORE[session_id]

#         print(
#             f"[+] Session for '{user}' "
#             f"has been securely destroyed."
#         )

#         print(
#             " The session token is now permanently invalid."
#         )

#     else:

#         print(
#             "[!] Session not found or already invalidated."
#         )


# def try_use_session(session_id):

#     if session_id in SESSION_STORE:

#         print(
#             f"[+] Session active for: "
#             f"{SESSION_STORE[session_id]['username']}"
#         )

#     else:

#         print(
#             "[!] Access Denied: Session does not exist."
#         )


# # Simulate login, logout,
# # and post-logout token reuse attempt

# sid = login("alice")
# try_use_session(sid)   # Should succeed
# logout(sid)
# try_use_session(sid)   # Should fail



###################################################################################
# Program 12: Session Activity Monitor
# Detects anomalous patterns that indicate
# session theft or sharing

# def analyze_session_activity(session_events):
#     """
#     Analyzes a list of session events for anomalies.
#     Each event is a dict with 'location'
#     and 'timestamp' keys.
#     """

#     locations = [
#         event["location"]
#         for event in session_events
#     ]

#     unique_loc = list(set(locations))

#     print("[~] Analyzing session activity log...")

#     print(f" Total requests : {len(session_events)}")

#     print(f" Unique locations : {len(unique_loc)}")

#     if len(unique_loc) > 1:

#         print(
#             "[!] ANOMALY DETECTED: "
#             "Session active from multiple locations!"
#         )

#         print(
#             f" Locations: {', '.join(unique_loc)}"
#         )

#         print(
#             " Recommended action: "
#             "Force logout and require reauthentication."
#         )

#     else:

#         print(
#             f"[+] Activity Normal: "
#             f"All requests from {unique_loc[0]}."
#         )


# # Simulate normal activity

# normal_events = [

#     {
#         "location": "India",
#         "timestamp": "10:01"
#     },

#     {
#         "location": "India",
#         "timestamp": "10:15"
#     }
# ]

# analyze_session_activity(normal_events)

# print()

# # Simulate suspicious activity
# # (same session, two countries)

# suspicious_events = [

#     {
#         "location": "India",
#         "timestamp": "10:01"
#     },

#     {
#         "location": "Russia",
#         "timestamp": "10:03"
#     }
# ]

# analyze_session_activity(suspicious_events)