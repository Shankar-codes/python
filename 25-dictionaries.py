DevOpswithEllamma = {
    "Course": "DevOps",
    "Trainer": "Shankar",
    "Duration": "45 Hrs",
    "Mode": "Online"
}

print(DevOpswithEllamma)

# accessing the dictionary elements
print(f"Course : {DevOpswithEllamma["Course"]}")
print(f"Trainer : {DevOpswithEllamma["Trainer"]}")
print(f"Duration : {DevOpswithEllamma["Duration"]}")
print(f"Training Mode : {DevOpswithEllamma["Mode"]}")

# adding and updating the dictionary elements
DevOpswithEllamma["Course"]="DevSecOps"
print(DevOpswithEllamma["Course"])

# deleting the dictionary elements
DevOpswithEllamma.pop("Mode")
print(DevOpswithEllamma)

del DevOpswithEllamma["Course"]
print(DevOpswithEllamma)