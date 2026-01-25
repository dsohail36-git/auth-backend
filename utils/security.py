import bcrypt

def hash_password(password: str) -> bytes:
    # Fix: bcrypt requires bytes input and returns bytes hash
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
