#! /usr/bin/python3
# code to test out punctuation marks or symbols in generating a password


import string
import secrets

alpha = string.ascii_letters 
numeric = string.digits
symbol = string.punctuation
password_makeup = alpha + numeric + symbol

while True:
    password = ''.join(secrets.choice(password_makeup) for i in range(12))
    if (sum(c.islower() for c in password) >=3
        and sum(c.isupper() for c in password) >=3
        and sum(c.isdigit() for c in password) >=2
        and (c for c in password if password.count(symbol) >=2)):
        break
print(password)