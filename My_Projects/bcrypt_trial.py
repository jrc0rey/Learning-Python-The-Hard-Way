import bcrypt

password = b"fredcat246"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
    print("It's a match")
else:
    print("No way jose")
