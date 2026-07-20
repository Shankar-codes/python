def greetings():
    print("Hello Shankar! Have a nice day")
    
greetings()


# function with parametes asking name with prompt
def greet_user(name):
    print(f"Hello {name}! Have a nice day")
    
name=input("Enter the name: ")
greet_user(name)

# returning values from a function
def add_numbers(a,b):
    return a + b

result=add_numbers(10, 20)
print(f"The sum is : {result}")

# default parameters
def greet_student(name="student"):
    print(f"Hello {name}! Welcome to the DevOps course")
    
greet_student()
greet_student("Ellamma")


# keyword arguments
def student_details(name, age, subject):
    print(f"Name: {name}\nAge: {age}\nSubject: {subject}")

student_details("Shankar", 25, "DevOps")


# *args examples
def total_sum(*numbers):
    result = 0
    for num in numbers:
        result+=num
    return result

print(total_sum(5,6,5,6,5,6))

# **kwargs examples
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info