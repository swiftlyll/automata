import string
import secrets

# generate random password according to best practices 
# https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
chars = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(chars) for i in range (15))
    if (any(char.islower for char in password)
            and any(char.isupper() for char in password)
            and any(char.isdigit() for char in password)):
        break

print(password)