DevOpswithEllamma={
    "course":"DevOps",
    "Trainer":"Shankar",
    "Duration":"40 hrs"
}

for details in DevOpswithEllamma.values():
    print(details)
    
students_marks={
    "Shankar":95,
    "Ellamma":99,
    "Geetha":98
}

print("------Students marks sheets-------")
for student, marks in students_marks.items():
    print(f"{student}: {marks}")