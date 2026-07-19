DevOps = ["Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernetes", "Python"]
numbers = [1, 2, 3, 4]

# Functions
print(len(DevOps)) # length of the list
print(sorted(DevOps)) # list sorting ascending order
print(sum(numbers)) # sum of the list numbers

# Methods
print(DevOps.index("Terraform"))

# count = Shankar two times are there
names = ["Shankar", "Shankar", "Ellamma", "Thimmappa"]
print(names.count("Shankar"))

# printing the lists reverse
DevOps.reverse()
print(DevOps)

numberings = [8, 2, 6, 9]
numberings.sort()
print(numberings)

# Nested lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

# accesing the nested lists
print(matrix[0][0])

print(matrix[2][1])