class Calculator():
    def __init__(self):
        print("Calculated Results")
    def sum(self,a,b):
        return a+b
    def multiplication(self,a,b):
        return a*b
    def subtract(self,a,b):
        return a-b
    def squarea(self,a):
        return a*a
    def squareb(self,b):
        return b*b
    def divide(self,a,b):
        return a/b
    
obj= Calculator()
a = input('Enter a : ')
b = input("Enter b : ")
a = int(a)
b = int(b)
print("a =",a)
print("b =",b)

sum=obj.sum(a,b)
print("Calculated sum result of a and b = ",sum)
Xply = obj.multiplication(a,b)
print("Calculated multiplication result of a and b =",Xply)
substract=obj.subtract(a,b)
print("Calculated substraction result of a and b =",substract)
divide=obj.divide(a,b)
print("Calculated divide result of a and b =",divide)
squarea=obj.squarea(a)
print("Calculated square of a =",squarea)
squareb=obj.squareb(b)
print("Calculated square of b =",squareb)

    