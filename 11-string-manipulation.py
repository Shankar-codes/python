# string declaration
first_name = "Shankar"
second_name = "Ellamma"

print("first name :", first_name)
print("second name :", second_name)

# string concatenation
full_name = first_name + " " + second_name
print("Full name = ", full_name)

# string repetetion
greeting = "Hello "*3
print(greeting)

# string methods
message = f"   Hello, {first_name}"
print(message.strip()) # removes the spaces in left and right of the string
print(first_name.upper()) #  UPPERCASE
print(second_name.lower()) # lowercase

# replace the word
replace=message.replace("Hello", "Greetings")
print(replace.strip())

# accessing the string characters
course = "python"
print(course[0], course[1], course[2])

# string slicing
new_course = "DevOps Engineer"
print(new_course[0:6])
print(new_course[0:])
print(new_course[:4])