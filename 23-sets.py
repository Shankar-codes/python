# creating sets
DevOps = {"Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernates", "Linux"}

print(DevOps)

# Creating empty set
new_set=set()

# Set operations
set1={1,2,3,4}
set2={3,4,5,6}

# Union set
union_set=set1 | set2
print(union_set)

# Intersection
intersection=set1 & set2
print(intersection)

# Difference
difference= set1 - set2
print(difference)

# Symmetric difference
symmetric = set1 ^ set2
print(symmetric)