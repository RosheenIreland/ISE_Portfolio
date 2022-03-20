#Creating a calculator with if.. elif..else and functons(def)

def add(x, y): # To add two numbers 
    return x + y # Exits the function and returns sum

def subtract(x, y): 
    return x - y

def multiply(x,y):
    return x * y

def divide(x, y):
    return x / y


print("""
Select operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")

#Take input from user
Select = int(input("Enter choice(1, 2, 3, 4, 5):")) #converts value into an integer


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Conditional Statement (Loop)
if Select == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif Select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif Select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))


elif Select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

elif Select == 5:
    exit()
    
else:
    print("Invalid Input")