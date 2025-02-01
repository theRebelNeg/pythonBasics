#this method adds two numbers
def add(a,b):
    return a + b
#this method subtracts two numbers
def subtract(a,b):
    return a - b
#this method multiply two numbers
def multiply(a,b):
    return a * b
    
#this method divides two numbers
def divide(a,b):
    return a / b

print("choose your desired operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    user=input("Enter choices (1/2/3/4) : ")
    if user in ('1' , '2' ,'3' ,'4'):
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
        except ValueError:
            print("invalid input. please enter a valid number")
            continue
            
        if user=='1':
            print(num1, "+" ,num2, " = ",add(num1,num2))
        elif user=='2':
            print(num1, "-" ,num2, " = ",subtract(num1,num2))
        elif user=='3':              
            print(num1, "*" ,num2, " = ",multiply(num1,num2))
        elif user=='4':
            print(num1, "/" ,num2, " = ",divide(num1,num2))
            
            #check to see if user wants to continue calculations
        next_calculation=input("do another calulation ? (yes/no)")
        if next_calculation=='no':
            print("Goodbye!")
            break
    else:
        print("invalid value")

