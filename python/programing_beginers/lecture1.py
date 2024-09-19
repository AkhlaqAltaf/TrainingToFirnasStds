# print("HEY HOW ARE YOU..")


# a = 10 
# b = 20
# c  = b+a
# print(c)


# indentatio


class Calculator:

    def __init__(self):
        print("CONSTRUCTION...")

    def sum(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def multiplication(self,a,b):
        return a*b
    


obj = Calculator()


a = input('Enter a : ')
b = input("Enter b : ")
a = int(a)
b = int(b)

sum=obj.sum(a,b)
print(sum)
mult = obj.multiplication(a,b)

print(mult)































# a= int(input("Enter Digit 1  ")) 

# b =int(input("Enter Digit 2  ")) 

# print(a*b)

#print("My Cell Nunmber is 03317782810")
# OPERATIONS 
#  * Multiplication 
# / devision 
# - minus 
# + additions 



