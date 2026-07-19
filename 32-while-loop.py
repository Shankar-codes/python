i = 1
while i<=5:
    print(i)
    i+=1
    
    
sheep_count=1
while sheep_count<=10:
    print(f"Sheep {sheep_count}")
    sheep_count +=1
    
print("-------break example---------")
# break statement
sheep_count = 1
while sheep_count<=10:
    print(f"Sheep {sheep_count}")
    if sheep_count==5:
        print("That's enough counting")
        break
    sheep_count +=1
    
print("-------continue example---------")
# contine statement
sheep_count = 1
while sheep_count<=10:
    print(f"Sheep {sheep_count}")
    if sheep_count==5:
        sheep_count+=1
        print("That's not counting")
        continue
    sheep_count +=1