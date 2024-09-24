class Calculator2:


    def __init__(self):
        self.doc() 
        while True:
            operator = self.commands("PLEASE ENTER OPERATOR or Press 'n' to quit): ")
            if operator == "n":
                print("Exiting the calculator.")
                break
            
            try:
                a = float(self.commands("PLEASE ENTER a = "))
                b = float(self.commands("PLEASE ENTER b = "))
            except ValueError:
                print("Sorry for incovenience. Please try again and enter valid number!...")
                continue
            finally:
                print("Thanks for choosing us...")

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