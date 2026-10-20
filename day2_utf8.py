print(chr(65))
print(ord('A'))

def safe_decode_utf8(raw_bytes: bytes) -> str:
    """Decode bytes to string, rejecting non-UTF-8 sequences."""
    try:
        # errors='strict' raises UnicodeDecodeError on bad bytes
        return raw_bytes.decode('utf-8', errors='strict')
    except UnicodeDecodeError as e:
        raise ValueError(f'Input is not valid UTF-8: {e}')
# Accepting raw socket data or file reads:
raw = b'\xff\xf invalid bytes'
# safe_decode_utf8(raw) # ❌ raises ValueError — bad encoding detected
# raw = b'Hello, World!'
# print(type(raw))
s=safe_decode_utf8(raw)
print(type(s))

# DANGER: Using byte length for character limits
# text = '😊😊😊😊😊' # 5 emoji characters
# print(len(text)) # → 5 (characters)
# print(len(text.encode('utf-8'))) # → 20 (bytes! each emoji = 4 bytes)
# If your DB column is VARCHAR(10 bytes) but you check len(text):
# if len(text) <= 10: # 5 <= 10 → True (WRONG check!)
#     db.store(text) # ❌ Tries to store 20 bytes in 10-byte column →

# Correct approach — check BYTES for storage, CHARS for UX limits:
# MAX_CHARS = 200
# MAX_BYTES = 800 # Assuming up to 4 bytes per char
# def validate_text_storage(text: str) -> str:
#     if len(text) > MAX_CHARS:
#         raise ValueError(f'Too many characters: {len(text)}/{MAX_CHARS}')
#     if len(text.encode('utf-8')) > MAX_BYTES:
#         raise ValueError('Text too large in bytes for storage')
#     return text

# MAX_CHARS = 200
# MAX_BYTES = 800  # Match your DB/storage limit

# def validate_text_storage(text: str) -> str:
#     # 1. Character limit (UX)
#     if len(text) > MAX_CHARS:
#         raise ValueError(f'Too many characters: {len(text)}/{MAX_CHARS}')
    
#     # 2. Byte limit (storage)
#     byte_length = len(text.encode('utf-8'))
#     if byte_length > MAX_BYTES:
#         raise ValueError(f'Text too large: {byte_length}/{MAX_BYTES} bytes')
#     return text
# # ✅ Valid input
# # print(validate_text_storage("Hello"))
# # # ✅ Emoji within limit
# # print(validate_text_storage("😊😊"))
# # ❌ Too many bytes
# print(validate_text_storage("😊" * 300))


# blocked = ["admin"]
# user_input = "admi\u006E"  # looks like "admin"
# if user_input in blocked:
#     print("Blocked")
# else:
#     print("Allowed")  # ❌ bypass!
# “NFC joins, NFD splits, NFKC simplifies, NFKD simplifies + splits.”
# C = Combine, D = Decompose, K = Compatibility
import unicodedata
# text = "e\u0301"  # e + accent
# print(len(text))
# print(len(unicodedata.normalize("NFC", text)))

# text = "é"
# print(unicodedata.normalize("NFD", text))
# print(len(unicodedata.normalize("NFD", text)))

# text = "①"  # circled number
# print(unicodedata.normalize("NFKC", text))

# text = "①"
# print(unicodedata.normalize("NFKD", text))

# import unicodedata
# print("🔤 Unicode Normalization Demo (NFC vs NFD)\n")

# # Step 1: Two identical-looking words
# word1 = "café"          # NFC (usually typed)
# word2 = "cafe\u0301"    # NFD (e + combining accent)

# print("Original Words:")
# print("word1:", word1)
# print("word2:", word2)

# Step 2: Direct comparison
# print("\nAre they equal?")
# print(word1 == word2)  # ❌ False

# # Step 3: Length difference
# print("\nLength check:")
# print("len(word1):", len(word1))
# print("len(word2):", len(word2))

# Step 4: Apply NFC (compose)
# nfc1 = unicodedata.normalize("NFC", word1)
# nfc2 = unicodedata.normalize("NFC", word2)

# print("\nAfter NFC normalization:")
# print("nfc1:", nfc1)
# print("nfc2:", nfc2)
# print("Are equal after NFC?", nfc1 == nfc2)  # ✅ True

# Step 5: Apply NFD (decompose)
# nfd1 = unicodedata.normalize("NFD", word1)
# nfd2 = unicodedata.normalize("NFD", word2)

# print("\nAfter NFD normalization:")
# print("nfd1:", nfd1)
# print("nfd2:", nfd2)
# print("Are equal after NFD?", nfd1 == nfd2)  # ✅ True
# print("Length after NFD:", len(nfd1))
# print("Length after NFD:", len(nfd2))

# # Step 6: Show removing accents (bonus)
# ascii_text = ''.join(
#     ch for ch in nfd1 if not unicodedata.combining(ch)
# )
# print("\nAfter removing accents:")
# print("ASCII version:", ascii_text)

import unicodedata
print("🔤 NFKC vs NFKD Demo\n")
# Step 1: Compatibility characters
text = "① Ⅱ ℌ café"
print("Original text:")
print(text)

# # Step 2: Apply NFKC (normalize + simplify)
# nfkc = unicodedata.normalize("NFKC", text)

# print("\nAfter NFKC normalization:")
# print(nfkc)

# Step 3: Apply NFKD (normalize + decompose fully)
# nfkd = unicodedata.normalize("NFKD", text)

# print("\nAfter NFKD normalization:")
# print(nfkd)

# # Step 4: Remove accents (bonus)
# ascii_text = nfkd.encode("ascii", "ignore").decode("ascii")

# print("\nAfter removing accents (using NFKD):")
# print(ascii_text)

import unicodedata
print("🔤 Unicode Normalization Master Demo\n")
# Step 1: Mixed text (combining + compatibility characters)
text = "café cafe\u0301 ① ℌ"
print("Original text:")
print(text)
# Show raw comparison example
# word1 = "café"
# word2 = "cafe\u0301"

# print("\nDirect comparison (without normalization):")
# print("word1 == word2 ?", word1 == word2)  # ❌ False

# Step 2: NFC (compose)
# nfc = unicodedata.normalize("NFC", text)
# print("\n🔹 NFC (Composed - standard form):")
# print(nfc)

# Step 3: NFD (decompose)
# nfd = unicodedata.normalize("NFD", text)
# print("\n🔹 NFD (Decomposed - split characters):")
# print(nfd)
# print("Length after NFD:", len(nfd))

#Step 4: NFKC (compatibility + compose)
# nfkc = unicodedata.normalize("NFKC", text)
# print("\n🔹 NFKC (Simplify + composed):")
# print(nfkc)
# print(len(nfkc))

# # Step 5: NFKD (compatibility + decompose)
# nfkd = unicodedata.normalize("NFKD", text)
# print("\n🔹 NFKD (Simplify + decomposed):")
# print(nfkd)
# print(len(nfkd))


# # Step 6: Remove accents (using NFKD)
# ascii_text = nfkd.encode("ascii", "ignore").decode("ascii")
# print("\n🔹 After removing accents:")
# print(ascii_text)

# # Step 7: Compare after normalization
# print("\nComparison after NFC normalization:")
# print(
#     unicodedata.normalize("NFC", word1) ==
#     unicodedata.normalize("NFC", word2)
# )  # ✅ True

# import unicodedata
# text = "café ①"
# nfkc = unicodedata.normalize("NFKC", text)
# nfkd = unicodedata.normalize("NFKD", text)
# print("NFKC:", nfkc)
# print("NFKD:", nfkd)
# print("Length NFKC:", len(nfkc))
# print("Length NFKD:", len(nfkd))

# import unicodedata
# # Fullwidth Latin letters look identical to normal ones
# fullwidth_admin = '\uff41\uff44\uff4d\uff49\uff4e'  # 'admin' in fullwidth
# normal_admin = 'admin'
# # Step 1: Direct comparison (without normalization)
# print("Without normalization:")
# print(fullwidth_admin == normal_admin)  # ❌ False — bypass possible!
# # Step 2: Vulnerable check
# if fullwidth_admin == 'admin':
#     print('admin detected')  # ❌ This will NOT run
# # Step 3: Apply NFKC normalization
# nfkc_admin = unicodedata.normalize('NFKC', fullwidth_admin)
# print("\nAfter NFKC normalization:")
# print(nfkc_admin == normal_admin)  # ✅ True
# print("Normalized value:", nfkc_admin)
# # Step 4: Secure check
# if nfkc_admin == 'admin':
#     print('admin detected (secure)')  # ✅ This WILL run


# import unicodedata
# import urllib.parse
# import html
# import re

# def secure_normalize(
#     raw_input: str,
#     max_len: int = 500,
#     allow_pattern: str = r'^[a-zA-Z0-9 _.,!?-]+$'
# ) -> str:
#     """
#     Full normalization pipeline:
#     1. Length pre-check (fast reject)
#     2. URL decode (handle %XX encoding)
#     3. Unicode NFKC normalization
#     4. Lowercase (optional normalization)
#     5. Strip whitespace
#     6. Length check after normalization
#     7. Allow-list validation
#     8. HTML escape (safe output)
#     """

#     # Step 1: Fast length pre-check
#     if not raw_input or len(raw_input) > max_len * 4:
#         # raw_input = "%3C%3C%3C%3C",Length = 12,,,<<<<
#         raise ValueError('Input empty or far too long')

#     # Step 2: URL decode (max 3 passes)
#     data = raw_input
#     for _ in range(3):
#         decoded = urllib.parse.unquote(data)
#         if decoded == data:
#             break
#         data = decoded

#     # Step 3: Unicode normalization (NFKC)
#     data = unicodedata.normalize('NFKC', data)

#     # Step 4: Lowercase (use it!)
#     data = data.lower()

#     # Step 5: Strip whitespace
#     data = data.strip()

#     # Step 6: Length check after normalization
#     if len(data) > max_len:
#         raise ValueError(f'Input exceeds {max_len} character limit')

#     # Step 7: Allow-list validation
#     if not re.match(allow_pattern, data):
#         raise ValueError('Input contains disallowed characters')

#     # Step 8: Escape for safe output
#     return html.escape(data)


# 🔍 Test cases
# print(secure_normalize('Hello World'))        # ✅ ok
# print(secure_normalize('ａｄｍｉｎ '))          # ✅ becomes 'admin'
# print(secure_normalize('%3Chello%3E'))        # ❌ rejected (<hello> not allowed)