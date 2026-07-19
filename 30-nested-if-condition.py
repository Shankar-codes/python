day = "saturday"
is_raining = True

if day == "saturday" or day == "sunday":
    if not is_raining:
        print("Let's visit Mysore")
    else:
        print("It's raining. let's stay in home.")
else:
    print("It's weekday, let's wait for the weekend")