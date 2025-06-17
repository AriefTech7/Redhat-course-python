# password_exceptions.py

class PasswordError(Exception):
    """Base class untuk semua pengecualian terkait password"""
    pass

class PasswordTooShortError(PasswordError):
    def __init__(self, message="Password terlalu pendek"):
        self.message = message
        super().__init__(self.message)

class PasswordMissingDigitError(PasswordError):
    def __init__(self, message="Password harus mengandung setidaknya satu angka"):
        self.message = message
        super().__init__(self.message)

class PasswordMissingSpecialCharError(PasswordError):
    def __init__(self, message="Password harus mengandung setidaknya satu karakter khusus (!@#$%^&*)"):
        self.message = message
        super().__init__(self.message)