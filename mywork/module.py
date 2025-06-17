# password_validator.py
from error import PasswordTooShortError, PasswordMissingDigitError, PasswordMissingSpecialCharError

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError()

    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigitError()

    special_chars = "!@#$%^&*"
    if not any(char in special_chars for char in password):
        raise PasswordMissingSpecialCharError()

    print("✅ Password valid")