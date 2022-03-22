# This is a simple random password generator

import random # Imports a module for allowing the password to be randomised
import string 

print('Hello, Welcome to the Password Generator!')

lenght = int(input('\nEnter lenght of password: ')) # Getting Users input


lower = string.ascii_lowercase 
upper = string.ascii_uppercase
num = string.digits 
symbols = string.punctuation

all = lower + upper + num + symbols # Calling each catagory of characters

temp = random.sample(all,lenght) 

password = "".join(temp)

print(password)