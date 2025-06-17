# main.py
from module import validate_password
from error import PasswordTooShortError, PasswordMissingDigitError, PasswordMissingSpecialCharError

try:
    pwd = input("Masukkan password: ")
    validate_password(pwd)
except PasswordTooShortError as e:
    print("❌ Kesalahan:", e.message)
except PasswordMissingDigitError as e:
    print("❌ Kesalahan:", e.message)
except PasswordMissingSpecialCharError as e:
    print("❌ Kesalahan:", e.message)
except Exception as e:
    print("Kesalahan umum:", e)