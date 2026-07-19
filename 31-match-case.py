day = input("Enter the day ")

print(day.lower())
match day.lower():
    case "monday":
        print("Start of the work week")
    case "friday":
        print("It's almost weekend!")
    case "saturday" | "sunday":
        print("It's weekend!")
    case _:
        print("Just another weekday")