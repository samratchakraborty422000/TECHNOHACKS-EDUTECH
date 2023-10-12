print("WELCOME TO SAMRAT'S CALCULATOR")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select not in [1,2,3,4]:
    print("INVALID INPUT")
    select = int(input("Select operations form 1, 2, 3, 4 :"))
 
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
 
if select == 1:
    print(a, "+",b, "=",
                    add(a,b))
elif select == 2:
    print(a, "-",b, "=",
                    sub(a,b))
elif select == 3:
    print(a, "x",b, "=",
                    mul(a,b))
elif select == 4:
    print(a, "/",b, "=",
                    div(a,b))
else:
    print("Invalid input")