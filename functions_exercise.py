# simple calculator
def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y 
def divide(x, y):
    if y == 0:
     return "error! Diviosn by 0"
    return x // y 
def exponentiate(x, y):
    return x ** y 
def modulus(x, y):
    return x % y
def floor_division(x, y):
   if y == 0: 
      return "error! Diviosn by 0"
   return x // y 
print("Calculator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponentiate")
print("6.Modulo")
print("7.Floor division")
print("8.Exit")

while True:
      choice = int(input("Enter your choice(1/2/3/4/5//6/7):"))
      if choice == 1:
        print ("Enter two numbers")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(add(x,y))
      elif choice == 2:
              print ("Enter two numbers")
              x = int(input("Enter first number: "))
              y = int(input("Enter second number: "))
              print(subtract(x,y))
      elif choice == 3:
        print ("Enter two numbers")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(multiply(x,y))
      elif choice == 4:
          print ("Enter two numbers")
          x = int(input("Enter first number: "))
          y = int(input("Enter second number: "))
          print(divide(x,y))
      elif choice == 5:
        print ("Enter two numbers")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(exponentiate(x,y))
      elif choice == 6:
         print ("Enter two numbers")
         x = int(input("Enter first number: "))
         y = int(input("Enter second number: "))
         print(modulus(x,y))
      elif choice == 7:
        print ("Enter two numbers")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(floor_division(x,y))
      elif choice == 8:
         print("Exit")
         break
     
      else:
            print("Invalid output")
    


#Second Exercise
#try in class

# A student can apply for admission by providing their name, age, email, grade
# The function should check if the student is eligible for admission based 
# on grade
# If the student is eligible, 
# the function should return a message saying "Congratulations {name}, 
# you have been admitted to our school"
# If the student is not eligible, the function should return a message saying
#  "Sorry {name}, you are not eligible for admission"
# If the student is eligible, the function should also return the student's 
# profile which includes their name, age, email, and grade.
# If the student is not eligible, the function should not return the profile.
# The function should also store the student's profile in a local storage
# (a dictionary) if they are eligible for admission.


def student_profile(name, age, email, grade):
    profile = {
        'name': name,
        'age' : age,
        'email': email,
        'grade': grade
     }
    return profile
print("Welcome to MIRN College!")
print("1.Apply for admmision")
print("2.Exit")
while True:
      choice = int(input("Enter your choice: "))
      if choice == 1:
        student_input = input("Enter your name, age, email and grade with spaces in between: ")
        print(student_input)
        name, age, email, grade = student_input.split()
      
        if grade == ['A','B','C'] :
            print(f"Congratulations {name}, you have been admitted to our school. Your profile is {student_profile(name, age, email, grade)}")
       
        else:
            print(f"Sorry {name}, you are not eligible for admission.")
      elif choice == 2:
        print ("Thank you for visiting our portal")
        break
    

     
            
   
    