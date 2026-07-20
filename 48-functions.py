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
