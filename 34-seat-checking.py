available_seat = 5
while available_seat > 0:
    booking = input("Do you want to book the seat? (yes/no):").lower()
    if booking=="yes":
        available_seat-=1
        print(f"Seat booked!. available seates: {available_seat} ")
    else:
        print(f"No booking made. available seates: {available_seat}")
print("All seats are booked")