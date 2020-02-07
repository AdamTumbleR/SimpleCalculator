def Add(x,y):
    return x+y
def Substract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x,y):
    return x/y
def Power(x,y):
    return x**y

print("Select operation: ")
print ("1. Add")
print ("2. Substract")
print ("3. Multiply")
print ("4. Divide")
print ("5. Power")
choice = input("Enter number of operation 1-5: ")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if choice == "1":
    print(num1,"+",num2,"=",Add(num1,num2))
if choice == "2":
    print(num1,"-",num2,"=",Substract(num1,num2))
if choice == "3":
    print(num1,"*",num2,"=",Multiply(num1,num2))
if choice == "4":
    print(num1,"/",num2,"=",Divide(num1,num2))
if choice == "5":
    print(num1,"**",num2,"=",Power(num1,num2))




