
while(True):
        a = input("please enter num1")
        b = input("PLEASE enter num2")
        try:      
            a = int(a)
            b = int(b)

            sum = a+b
            print(sum)
        except Exception as e:
              print(e)
        finally:
              print("PROGRAM EXECUTED..")      