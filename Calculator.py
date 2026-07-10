#main menu
menu = """
====== Utility Calculator ======
1. Square
2. Cube
3. Addition
4.Subtraction
5. Multiplication
6. Division
7. Exit
"""
def num_square(n):
        return n * n

def num_cube(num):
      return num * num * num

def addition(a,b):
      return a + b

def subtraction(a,b):
      return a - b

def multi(a,b):
      return a * b

def division(a,b):
            return a / b

def exit_program():
      print("thankyou for using utility calculator😊 ")

while True:
     print(menu)
     user = input("enter your choice: ")
     if user =="1":
           n = int(input("enter your number for square: "))
           result = num_square(n)
           print("answer is: ",result)
         


     elif user == "2":
        num = int(input("Enter your number for cube: "))
        cube = num_cube(num)
        print("answer is: ",cube)
       

     elif user == "3":
           a = int(input("enter your first number: "))
           b = int(input("enter your second number: "))
           add = addition(a,b)
           print("answer is: ",add)

     elif user == "4":
           a = int(input("enter your first number: "))
           b = int(input("enter your second number: "))
           sub = subtraction(a,b)
           print("answer is: ",sub)


     elif user == "5":
           a = int(input("enter your first number: "))
           b = int(input("enter your second number: "))
           multiplication = multi(a,b)
           print("answer is: ",multiplication)


     elif user == "6":
           a = int(input("enter your first number: "))
           b = int(input("enter your second number: "))
           try:
                 divide = division(a,b)
                 print("answer is: ",divide)
           except ZeroDivisionError:
                 print("number can't devide by zero")
           except ValueError:
            	print("pls enter only number")
          
                 



     elif user == "7":
           exit_program()
           break

     else:
           print("invalid choice🤔")
