#! /usr/bin/python3
# password generator
# Parameters: length, complexity

from curses.ascii import isdigit
import secrets
import string
import sys
import math

def get_number_of_arguments():
    # 1 or 3 or more arguments we automatically print the help message
    # the first argument is the name of the script which means no values were passed
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        return 0
    elif len(sys.argv) == 2:
        return 1
    else: 
        len(sys.argv) == 3
        return 2


def how_to_use_message():
    print(
        'Usage: \npwgen.py <length> <complexity>', 
        '\n',
        '\nExample:\npwgen.py 12 uc',
        '\nGenerates password 12 characters long containing only uppercase letters'
        '\n',
        '\n\t<length> = a number, greater than 4 but less than 101',
        '\n\t<complexity> = a one or two letter code, default d is used if empty:',                    
        '\n\t\tuc = uppercase',
        '\n\t\td = uppercase and lowercase',
        '\n\t\tn = uppercase, lowercase, include numbers',        
        '\n\t\ts = uppercase, lowercase, include symbols',
        '\n\t\tns = uppercase, lowercase, include numbers and symbols',
        '\n'
        )    

def show_message_valid_password(passLength):
    print(f'Password Length is VALID: {passLength} \n')

def show_message_valid_complexity(passwordComplexity):
    print(f'Password Complexity is VALID: {passwordComplexity} \n')

def check_passwordlength_is_number():
    passLength =  sys.argv[1]
    return passLength.isdigit()

def is_PasswordLength_valid(passLength):
    if passLength > 4 and passLength < 101 or passLength == 4:        
        return True
    else:
        return False

def is_PasswordComplexity_valid(passComplexity):
    if passComplexity in ('d','uc','n','s','ns'):      
        return True
    else:        
        return False        

def main():
    number_of_arguments = get_number_of_arguments()
    
    
if __name__ == "__main__":
    main()    


def get_password(number_of_arguments, passLength, passwordComplexity):
    if number_of_arguments == 0:
        how_to_use_message()
    elif number_of_arguments == 1:
        if check_passwordlength_is_number() == True:
            passLength = int(passLength)
            passwordComplexity = 'd'
            password = generate_password(passLength, passwordComplexity)
            print('

'''
complexitymaintenance = 3

if parameter_count == 2:    
    passwordComplexity = sys.argv[2]
    passwordComplexity = str(passwordComplexity)
else:    
    passwordComplexity = 'd'






def passwordGenerator(passLength, passComplexity):
    alphabet = string.ascii_letters
    alphanumeric = string.ascii_letters + string.digits
    alphanumericsymbols = string.ascii_letters + string.digits + string.punctuation
    symbols = string.punctuation
    
    if passComplexity == 'd':        
        while True: 
            complexitymaintenance = 2
            cm = (math.floor(passLength/complexitymaintenance))
            password = ''.join(secrets.choice(alphabet) for i in range(passLength))
            if (any(c.islower() for c in password) >= cm 
                and any(c.isupper() for c in password)>= cm):
                break
            return password
    
    if passComplexity == 's':
        while True:            
            complexitymaintenance = 3
            cm = (math.floor(passLength/complexitymaintenance))
            password = ''.join(secrets.choice(alphanumericsymbols) for i in range(passLength))                     
            if (any(c.islower() for c in password) >= cm
                and any(c.isupper() for c in password) >= cm
                and sum(c.isdigit() for c in password) >= cm):
                    break
            return password   

    if passComplexity == 'n':
        while True:
            complexitymaintenance = 4
            cm = (math.floor(passLength/complexitymaintenance))
            password = ''.join(secrets.choice(alphanumericsymbols) for i in range(passLength))                     
            if (any(c.islower() for c in password) >= cm
                and any(c.isupper() for c in password) >= cm
                and sum(c.isdigit() for c in password) >= cm):
                    break
            return password    


    if passComplexity == 'ns':
        while True:
            complexitymaintenance = 4
            cm = (math.floor(passLength/complexitymaintenance))
            password = ''.join(secrets.choice(alphanumeric) for i in range(passLength))                     
            if (any(c.islower() for c in password) >= cm
                and any(c.isupper() for c in password) >= cm
                and sum(c.isdigit() for c in password) >= cm
                and (c for c in password if password.count(symbols) >=cm)):
                    break
            return password           

    if passComplexity == 'uc':
        while True:
            complexitymaintenance = 4
            cm = (math.floor(passLength/complexitymaintenance))        
            password = ''.join(secrets.choice(alphabet) for i in range(passLength))
            if (all(c.isupper() for c in password)):
                break                
        return password            

if parameter_count == 1:
    if validatePasswordLength(passLength) == True:        
        password = passwordGenerator(passLength,passwordComplexity)
        print('VALID Length:',passLength, '\nDefault Complexity:',passwordComplexity)
        print('Password:',password)
    else:
        print('INVALID Length:',passLength)

if parameter_count == 2:
    if validatePasswordLength(passLength) == True:
        if validatePasswordComplexity(passwordComplexity) ==True:
            password = passwordGenerator(passLength,passwordComplexity)
            print('VALID Length:',passLength, '\nVALID Complexity code:',passwordComplexity)
            print('Password:',password)
        else: 
            print('VALID Length:',passLength, '\nINVALID Complexity code:',passwordComplexity)           
    else:
        if validatePasswordComplexity(passwordComplexity) ==True:
            print('INVALID Length:',passLength,'\nVALID Complexity code:',passwordComplexity)
        else:
            print('INVALID Length:',passLength,'\nINVALID Complexity code:',passwordComplexity)
sys.exit()
'''