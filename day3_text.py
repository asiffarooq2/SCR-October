import re

# Conservative RFC 5321 pattern — rejects unusual but technically valid addresses
# This is appropriate for most web applications
EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9][a-zA-Z0-9._%\-+]{0,63}@'
    r'[a-zA-Z0-9][a-zA-Z0-9\-]{0,62}(?:\.[a-zA-Z0-9\-]{1,63})*'
    r'\.[a-zA-Z]{2,63}$'
)
def reject_invalid_email(email: str) -> str:
    email = email.strip().lower()
    # Length check (RFC limit)
    if len(email) > 254:
        raise ValueError('Email address too long')
    # Pattern validation
    if not EMAIL_PATTERN.match(email):
        raise ValueError('Email format not accepted')
    return email

# ✅ Valid cases
print(reject_invalid_email('user@example.com'))
print(reject_invalid_email('user+tag@sub.domain.in'))

# ❌ Invalid cases
print(reject_invalid_email('<script>@evil.com'))
print(reject_invalid_email('@nodomain'))


# import re

# # International phone: optional + then 7–15 digits (E.164-like)
# PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{6,14}$')

# def reject_invalid_phone(phone: str) -> str:
#     # Normalize: remove spaces, dashes, brackets, dots
#     normalized = re.sub(r'[\s\-().]+', '', phone.strip())

#     # Validate
#     if not PHONE_PATTERN.match(normalized):
#         raise ValueError('Invalid phone number format')

#     return normalized


# ✅ Valid
# print(reject_invalid_phone('+919876543210'))

# ⚠️ This will FAIL (starts with 0, not allowed by regex)
# print(reject_invalid_phone('(098) 765-4321'))

# ❌ Invalid
# print(reject_invalid_phone('not-a-phone'))
# print(reject_invalid_phone('00000000000000000'))


# def reject_unexpected_fields(data: dict, allowed_fields: set) -> dict:
#     """
#     Prevents mass assignment attacks.
#     Mass assignment: attacker sends extra fields (isAdmin=true)
#     that get blindly mapped to a model object.
#     """
#     unexpected = set(data.keys()) - allowed_fields

#     if unexpected:
#         raise ValueError(f'Unexpected fields not allowed: {unexpected}')

#     return data

# ALLOWED_REGISTER_FIELDS = {'username', 'email', 'password', 'age'}

# # Attacker sends:
# malicious_data = {
#     'username': 'attacker',
#     'email': 'hack@evil.com',
#     'password': 'pass1234',
#     'age': 25,
#     'isAdmin': True,        # Injection attempt!
#     'role': 'superadmin',   # Injection attempt!
# }
# # ❌ Will raise error
# reject_unexpected_fields(malicious_data, ALLOWED_REGISTER_FIELDS)

# import re
# Coupon validation pattern
# COUPON_PATTERN = re.compile(r'^[A-Z0-9]{4,12}$')


# def create_order(user_id, product_id, quantity, coupon_code):
#     """Dummy function to simulate order creation"""
#     return {
#         "status": "success",
#         "user_id": user_id,
#         "product_id": product_id,
#         "quantity": quantity,
#         "coupon": coupon_code
#     }

# def process_order(user_id, product_id, quantity, coupon_code=None):
#     """Fail fast at first invalid input — never partial processing."""
#     # Check 1: user_id
#     if not isinstance(user_id, int) or user_id <= 0:
#         raise ValueError('Invalid user_id')

#     # Check 2: product_id
#     if not isinstance(product_id, int) or product_id <= 0:
#         raise ValueError('Invalid product_id')

#     # Check 3: quantity
#     if not isinstance(quantity, int) or quantity <= 0:
#         raise ValueError('Invalid quantity')

#     # Check 4: coupon
#     if coupon_code is not None:
#         coupon_code = str(coupon_code).strip().upper()

#         if not COUPON_PATTERN.fullmatch(coupon_code):
#             raise ValueError('Invalid coupon code format')

#     # If all validations pass
#     return create_order(user_id, product_id, quantity, coupon_code)

# test_cases = [
#     # ✅ Valid inputs
#     (1, 101, 2, "SAVE10"),
#     (2, 202, 1, None),

#     # ❌ Invalid user_id
#     (-1, 101, 2, "SAVE10"),

#     # ❌ Invalid product_id
#     (1, -5, 2, "SAVE10"),

#     # ❌ Invalid quantity
#     (1, 101, 0, "SAVE10"),

#     # ❌ Invalid coupon (lowercase + special char)
#     (1, 101, 2, "save@10"),

#     # ❌ Invalid coupon (too short)
#     (1, 101, 2, "A1"),
# ]
# # Run tests
# for i, case in enumerate(test_cases, 1):
#     print(f"\nTest Case {i}: {case}")
#     try:
#         result = process_order(*case)
#         print("✅ Success:", result)
#     except ValueError as e:
#         print("❌ Error:", e)

# from typing import Optional

# def require_string(value: Optional[str], field_name: str,
#                    min_len: int = 1, max_len: int = 200) -> str:
#     """Handle all variants of 'missing' string input."""

#     # Check None
#     if value is None:
#         raise ValueError(f'{field_name} is required (got None)')

#     # Check non-string types
#     if not isinstance(value, str):
#         raise TypeError(
#             f'{field_name} must be a string, got {type(value).__name__}'
#         )

#     # Strip whitespace
#     stripped = value.strip()

#     # Check empty after stripping
#     if not stripped:
#         raise ValueError(f'{field_name} cannot be empty or whitespace-only')

#     # Length checks
#     if len(stripped) < min_len:
#         raise ValueError(f'{field_name}: minimum length is {min_len}')

#     if len(stripped) > max_len:
#         raise ValueError(f'{field_name}: maximum length is {max_len}')

#     return stripped


# # 🔹 Test Cases
# tests = [
#     (None, 'name'),
#     ('', 'name'),
#     ('welcome'*10, 'name'),
#     ('Ali', 'name'),
# ]

# for t in tests:
#     try:
#         print("Input:", t[0])
#         result = require_string(t[0], t[1])
#         print("✅ Output:", result)
#     except Exception as e:
#         print("❌ Error:", e)
#     print("-" * 40)


# Python integers have arbitrary precision — no native overflow
# But other systems (C, Java, JavaScript) do overflow
# When interacting with external systems, clamp to safe ranges

# INT32_MAX = 2_147_483_647   # 2^31 - 1
# INT32_MIN = -2_147_483_648  # -2^31

# def validate_int32_safe(value, field_name='value'):
#     try:
#         n = int(value)
#     except (ValueError, TypeError):
#         raise TypeError(f'{field_name} must be an integer')

#     if n > INT32_MAX or n < INT32_MIN:
#         raise ValueError(f'{field_name} out of 32-bit integer range')

#     return n

# # 🔹 Test Cases
# tests = [
#     2147483647,   # ✅ max
#     2147483648,   # ❌ overflow
#     -2147483649,  # ❌ underflow
#     "123",        # ✅ string convertible
#     "abc",        # ❌ invalid type
# ]
# for t in tests:
#     try:
#         print(f"Input: {t}")
#         print("✅ Output:", validate_int32_safe(t))
#     except Exception as e:
#         print("❌ Error:", e)
#     print("-" * 40)


# from typing import Optional

# def validate_optional_bio(bio: Optional[str]) -> Optional[str]:
#     """
#     Bio is optional — None is acceptable.
#     But if provided, it must not be empty string or whitespace.
#     """

#     # Case 1: Not provided
#     if bio is None:
#         return None  # ✅ valid

#     # Type check (important improvement)
#     if not isinstance(bio, str):
#         raise TypeError("Bio must be a string")

#     # Normalize
#     stripped = bio.strip()

#     # Reject empty or whitespace-only
#     if not stripped:
#         raise ValueError('Bio cannot be empty if provided — omit it instead')

#     # Length check
#     if len(stripped) > 500:
#         raise ValueError('Bio too long')

#     return stripped

# # 🔹 Test cases
# tests = [
#     None,
#     "Hello!",
#     "",
#     "   ",
#     "A" * 501
# ]
# for t in tests:
#     try:
#         print("Input:", repr(t))
#         print("✅ Output:", validate_optional_bio(t))
#     except Exception as e:
#         print("❌ Error:", e)
#     print("-" * 40)


# import unicodedata

# # Invisible characters attackers use to bypass checks
# INVISIBLE_CHARS = {
#     '\u200b',  # Zero-width space
#     '\u200c',  # Zero-width non-joiner
#     '\u200d',  # Zero-width joiner
#     '\ufeff',  # BOM / zero-width no-break space
#     '\u00ad',  # Soft hyphen
#     '\u034f',  # Combining grapheme joiner
# }
# def reject_invisible_characters(text: str) -> str:
#     if not isinstance(text, str):
#         raise TypeError("Input must be a string")

#     for char in text:
#         # Explicit deny-list
#         if char in INVISIBLE_CHARS:
#             raise ValueError(
#                 f'Invisible character detected: U+{ord(char):04X}'
#             )

#         # Unicode category check
#         cat = unicodedata.category(char)
#         if cat in ('Cf', 'Cs'):  # Format chars, surrogates
#             raise ValueError(f'Disallowed Unicode category: {cat}')

#     return text

# # 🔹 Tests
# print(reject_invisible_characters('admin'))           # ✅ OK
# print(reject_invisible_characters('adm\u200bin'))     # ❌ raises


# import pytest

# class TestValidateAge:
#     """Systematic boundary testing for age validation."""

#     def validate_age(self, age):
#         # Type check (safer than string tricks)
#         if not isinstance(age, int):
#             raise TypeError('Age must be integer')

#         a = age

#         # Range check
#         if not (0 <= a <= 120):
#             raise ValueError('Age must be 0-120')

#         return a

#     # ── Valid cases ────────────────────────────────────────────
#     def test_minimum_valid(self):
#         assert self.validate_age(0) == 0

#     def test_just_above_min(self):
#         assert self.validate_age(1) == 1

#     def test_normal_case(self):
#         assert self.validate_age(25) == 25

#     def test_just_below_max(self):
#         assert self.validate_age(119) == 119

#     def test_maximum_valid(self):
#         assert self.validate_age(120) == 120

#     # ── Invalid cases ──────────────────────────────────────────
#     def test_below_minimum(self):
#         with pytest.raises(ValueError):
#             self.validate_age(-1)

#     def test_above_maximum(self):
#         with pytest.raises(ValueError):
#             self.validate_age(121)

#     def test_float(self):
#         with pytest.raises(TypeError):
#             self.validate_age(25.5)

#     def test_string(self):
#         with pytest.raises(TypeError):
#             self.validate_age('abc')

#     def test_empty(self):
#         with pytest.raises(TypeError):
#             self.validate_age('')

#     def test_none(self):
#         with pytest.raises(TypeError):
#             self.validate_age(None)

#     def test_very_large(self):
#         with pytest.raises(ValueError):
#             self.validate_age(9999999)

#     def test_very_negative(self):
#         with pytest.raises(ValueError):
#             self.validate_age(-9999999)


import urllib.parse
def decode_and_check(raw: str) -> str:
    # Step 1: Decode multiple times (important for obfuscation)
    for _ in range(3):
        decoded = urllib.parse.unquote(raw)
        if decoded == raw:
            break
        raw = decoded

    # Step 2: Convert to lowercase
    decoded_lower = raw.lower()

    # Step 3: Dangerous patterns
    dangerous = ['<script', 'javascript:', 'onerror=', 'onload=']

    # Step 4: Check for attack
    for pattern in dangerous:
        if pattern in decoded_lower:
            raise ValueError(f'Dangerous pattern after decoding: {pattern}')

    return raw

# 🔽 Test cases
inputs = [
    "hello world",
    "%3Cscript%3Ealert(1)%3C/script%3E",        
    "%6A%61%76%61%73%63%72%69%70%74%3Aalert(1)"
]

for i in inputs:
    try:
        result = decode_and_check(i)
        print(f"✅ SAFE: {result}")
    except ValueError as e:
        print(f"❌ BLOCKED: {i} → {e}")


# import urllib.parse

# def multi_decode(raw: str, max_passes: int = 5) -> str:
#     current = raw
#     for _ in range(max_passes):
#         decoded = urllib.parse.unquote(current)
#         if decoded == current:
#             return decoded
#         print("Decoded===",decoded)
#         current = decoded
#     raise ValueError('Too many decoding passes')

# def secure_check(user_input: str):
#     decoded = multi_decode(user_input)
#     lowered = decoded.lower()

#     dangerous = ['<script', 'javascript:', 'onerror=', 'onload=']

#     for pattern in dangerous:
#         if pattern in lowered:
#             raise ValueError(f"Blocked attack: {pattern}")

#     return decoded


# # 🔽 Test
# tests = [
#     "hello",
#     "%253Cscript%253E",
# ]

# for t in tests:
#     try:
#         print("SAFE:", secure_check(t))
#     except ValueError as e:
#         print("BLOCKED:", e)

# import urllib.parse
# import html
# import base64
# import unicodedata
# import re

# def full_decode_pipeline(raw: str) -> str:
#     """
#     Decode all common obfuscation techniques before validation.
#     """
#     data = raw

#     # Step 1: Multi-pass URL decoding
#     for _ in range(5):
#         prev = data
#         data = urllib.parse.unquote(data)
#         if data == prev:
#             break

#     # Step 2: HTML entity decoding
#     data = html.unescape(data)

#     # Step 3: Unicode normalization
#     data = unicodedata.normalize('NFKC', data)

#     # Step 4: Lowercase
#     data_lower = data.lower()

#     # Step 5: Base64 detection (simple heuristic)
#     try:
#         if len(data) % 4 == 0 and re.match(r'^[A-Za-z0-9+/]+=*$', data):
#             decoded_b64 = base64.b64decode(data).decode('utf-8', errors='ignore')
#             data_lower += ' ' + decoded_b64.lower()
#     except Exception:
#         pass

#     return data_lower


# def secure_check(raw: str) -> bool:
#     """
#     Allow only safe characters after full decoding.
#     """
#     normalized = full_decode_pipeline(raw)

#     # Allow-list (only safe characters)
#     if re.match(r'^[a-z0-9 _.,!?-]+$', normalized):
#         return True
#     return False


# -------------------------------
# 🔽 Test Inputs
# -------------------------------
test_inputs = [
    "hello world",
    "%3Cscript%3Ealert(1)%3C/script%3E",     # URL encoded
    "%253Cscript%253E",                     # double encoded
    "&lt;script&gt;alert(1)&lt;/script&gt;", # HTML encoded
    "c2NyaXB0",                             # base64 encoded 'script'
    "Normal_Text-123"
]

# -------------------------------
# 🔽 Run Tests
# -------------------------------
# for inp in test_inputs:
#     print("\nInput:", inp)
#     decoded = full_decode_pipeline(inp)
#     print("Decoded form:", decoded)

#     if secure_check(inp):
#         print("✅ SAFE INPUT")
#     else:
#         print("❌ BLOCKED (Malicious or Suspicious)")

# import html, json, re
# import urllib.parse

# class XSSDefense:

#     @staticmethod
#     def html_context(text: str) -> str:
#         """Escape for HTML body content — < > & " ' """
#         return html.escape(text, quote=True)

#     @staticmethod
#     def js_context(text: str) -> str:
#         """Escape for JavaScript string context."""
#         return json.dumps(text)  # Safe JS string

#     @staticmethod
#     def url_context(text: str) -> str:
#         """Encode for URL parameter context."""
#         return urllib.parse.quote(text, safe='')

#     @staticmethod
#     def css_context(text: str) -> str:
#         """Allow only safe characters in CSS context."""
#         if not re.match(r'^[a-zA-Z0-9 _\-]+$', text):
#             raise ValueError('Unsafe characters for CSS context')
#         return text


# # -------------------------------
# # 🔽 Test Example
# # -------------------------------
# user_input = '<script>alert(1)</script>'

# print("HTML Context:")
# print(f"<p>{XSSDefense.html_context(user_input)}</p>")

# print("\nJavaScript Context:")
# print(f"<script>var name = {XSSDefense.js_context(user_input)};</script>")

# print("\nURL Context:")
# print(f"https://example.com?q={XSSDefense.url_context(user_input)}")

# print("\nCSS Context:")
# try:
#     print(XSSDefense.css_context(user_input))
# except ValueError as e:
#     print("Blocked:", e)