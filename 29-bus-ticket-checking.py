age = int(input("Enter the age "))

if age < 5:
    print("Ticket is free")
elif age <= 12:
    print("Half ticket fare")
elif age >= 60:
    print("You get a senior citizen discount")
else:
    print("You pay full fare")
    