# Tuple
DevOps = ("Linux", "Shell", "Ansible", "Terraform", "Docker", "AWS")
print(DevOps)
numbers=(1, 2, 3)
# creating a tuple with one element:
single_element_tuple=("Kubernetes",)

# Accesing the tuple element
print(DevOps[3])

# Slicing the tuples
print(DevOps[1:4])

# Tuple concetation:
merged_tuples=DevOps + numbers
print(merged_tuples)

# Tuple repetetions
repeated_tuple=(numbers) * 3
print(repeated_tuple)

# Tuples - membership checking
print("jenkins" in DevOps)
print("AWS" in DevOps)
print("jenkins" not in DevOps)