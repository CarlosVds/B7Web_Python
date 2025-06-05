createPassword = int(input('Create a password with at least 8 non-sequential caracters: '))

password = createPassword

digitPassword = int(input("Digit your password: "))

if password == digitPassword:
    print("Valid password !!!")            
else:
    print("Invalid password!!!!")    
