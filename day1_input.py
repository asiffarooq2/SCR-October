# a=int(input("Enter the First Number"))
# b=int(input("Enter the Second Number"))
# c=a+b
# print(c)

# def validate_age(age_str):
#     """Validates age on the server — type + range check combined."""
#     if not age_str.isdigit():
#         return False, 'Age must be a whole number'
#     age = int(age_str)
#     if not (0 <= age <= 120):
#         return False, 'Age must be between 0 and 120'
#     return True, age
# result, value = validate_age(input('Enter age: '))
# print(result, value)

# class Validator:
#     @staticmethod
#     def validate_username(username):
#         return isinstance(username, str) and 3 <= len(username) <= 15
#     @staticmethod
#     def validate_age(age):
#         if not str(age).isdigit(): return False
#         return 18 <= int(age) <= 60
#     @staticmethod
#     def validate_email(email):
#         import re
#         return bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email))
# v = Validator()
# if Validator.validate_age('37'):
#     print('✅ Valid Age')
# else:
#     print('❌ Invalid Age')
# if Validator.validate_username('Harvinder'):
#     print('✅ Valid username')
# else:
#     print('❌ Invalid username')
# if Validator.validate_email('asif@example.com'):
#     print('✅ Valid email')
# else:
#     print('❌ Invalid email')

# def to_integer(value):
#     try:
#         return int(value)
#     except (ValueError, TypeError):
#         raise ValueError(f'Expected integer, got: {value!r}')
# print(to_integer('42')) # ✅ → 42
# print(to_integer('3.0')) # ❌ ValueError
# print(to_integer('abc')) # ❌ ValueError


import re
# ── Centralized Validator ──────────────────────────────────────
class Validator:
    @classmethod
    def validate_user_age(cls,age):
        # Type + range
        if not str(age).isdigit():
            return False, 'Age must be a number'
        age = int(age)
        if not (18 <= age <= 60):
            return False, 'Age must be between 18 and 60'
        return True, age
    @staticmethod
    def validate_username(username):
        # Allow-list + length
        if not re.match(r'^[a-zA-Z0-9_]{3,15}$', username):
            return False, 'Username: 3-15 chars, letters/numbers/_'
        return True, username
    @staticmethod
    def validate_age(age):
        # Type + range
        if not str(age).isdigit():
            return False, 'Age must be a number'
        age = int(age)
        if not (18 <= age <= 60):
            return False, 'Age must be between 18 and 60'
        return True, age
    # @staticmethod
    @classmethod
    def validate_email(cls,email):
    # Format pattern
        if not re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
            return False, 'Invalid email format'
        return True, email
    @staticmethod
    def validate_password(password):
    # Length
        if not (8 <= len(password) <= 64):
            return False, 'Password must be 8–64 characters'
        return True, password
        # ── Server-Side Registration Function ─────────────────────────
    def register_user(self,username, age, email, password):
        checks = [
        Validator.validate_username(username),
        Validator.validate_age(age),
        Validator.validate_email(email),
        Validator.validate_password(password),
        ]
        for ok, result in checks:
            if not ok:
                return f'❌ {result}'
        return '✅ Registration successful'
# ── Untrusted user input ───────────────────────────────────────
v=Validator()
# print(v.register_user('asif_99', '250', 'asif@mail.com', 'secureP@ss1'))
# → ✅ Registration successful
# print(v.register_user('a!@#', '200', 'notanemail', '1234'))
# # → ❌ Username: 3-15 chars, letters/numbers/_
print(Validator.validate_user_age(63))
# print(Validator.validate_email("has5@sgag.dh"))