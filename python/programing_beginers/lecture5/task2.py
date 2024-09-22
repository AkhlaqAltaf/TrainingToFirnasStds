
# BAD APPROACH

# class Calculator():
#   while(True):
#    print("Select Operation")
#    print("1. Add")
#    print("2. subtract")
#    print("3. Multiply")
#    print("4. Divide")

#    operation=input("Enter 1,2,3 or 4 for any operation = ")
#    if operation in ["1","2","3","4"]:
#       a=int(input("Enter any number = "))
#       b=int(input("Enter any number = "))
   
#       if operation == '1':
#                 result = a + b
#                 print(f"The sum of {a} and {b} is: {result}")

#       elif operation == '2':
#                 result = a - b
#                 print(f"The difference between {a} and {b} is: {result}")

#       elif operation == '3':
#                 result = a * b
#                 print(f"The product of {a} and {b} is: {result}")

#       elif operation == '4':
#                 if b != 0:
#                     result = a / b
#                     print(f"{a} divided by {b} is: {result}")
#                 else:
#                     print("Error! Division by zero.")

#    else:
#             print("Invalid input, please choose a valid operation.")
  
#    next_calculation = input("Do you want to do another calculation? Press any key to continue or 'n' to exit: ")
#    if next_calculation.lower() == 'n':
#             print("Exiting the calculator.")
#             break
            
# Calculator()




# GOOD APPROACH TO WRITE PYTHON CODE 



# class Calculator2:
#        def __init__(self) -> None:
#               self.doc()
#               while(True):
#                      operator = self.commands("PLEASE ENTER OPERATOR")
#                      if operator =="1":
#                             a = self.commands("PLEASE ENTER a")

                            


       
#        def add(self,a,b):
#               return a+b
#        def sub(self,a,b):
#               return a-b
       
#        def doc(self):
#                 print("Select Operation")
#                 print("1. Add")
#                 print("2. subtract")
#                 print("3. Multiply")
#                 print("4. Divide")

#        def commands(self,message):
#               coommand = input(message)
#               return coommand
       
#        def validator(self,command):
            
#             #   STRING VALIDATION 
#             # DIGIT VALIDATION 

#               pass
            
            
              

        




# Calculator2()


class Calculator2:
    def __init__(self):
        self.doc() 
        while True:
            operator = self.commands("PLEASE ENTER OPERATOR or Press 'n' to quit): ")
            if operator == "n":
                print("Exiting the calculator.")
                break
            

            a = float(self.commands("PLEASE ENTER a = "))
            b = float(self.commands("PLEASE ENTER b = "))

            if operator == "1":
                print(f"Result: {self.add(a,b)}")
            elif operator == "2":
                print (f"Result: {self.sub(a,b)}")
            elif operator == "3":
                print(f"Result: {self.multiply(a,b)}")
            elif operator == "4":
                print(f"Result: {self.divide(a,b)}")
            else:
                print("Invalid operator. Please try again.")

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def doc(self):
        print("Select Operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

    def commands(self, message):
        return input(message)

Calculator2()

