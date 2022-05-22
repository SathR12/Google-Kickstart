import random

alpha = list('abcdefghijklmnopqrstuvwxyz')
special = list("#@&*")
digits = [i for i in range(9)]

def solve(password):
    if any(i.isupper() for i in password) == False:
        password += random.choice(alpha).upper()
        
    if any(i.islower() for i in password) == False:
        password += random.choice(alpha)
        
    if any(i.isdigit() for i in password) == False:
        password += str(random.choice(digits))
        
    if any(i in special for i in password) == False:
        password += random.choice(special)
        
    if len(password) < 7:
        while len(password) < 7:
            password += random.choice(alpha)
            
    return password
        

cases = int(input())
for i in range(cases):
    length = int(input())
    password = input()
    print(f"Case #{i + 1}:", solve(password))
    
