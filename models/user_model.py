def find_user_by_email(email, db):
    return db.users.find_one({'email': email})

def create_user(email, hashed_password, db):
    # Fix: Store hashed_password as bytes or string (bcrypt returns bytes)
    db.users.insert_one({
        'email': email,
        'password': hashed_password  # Store as bytes; MongoDB can handle binary
    })
