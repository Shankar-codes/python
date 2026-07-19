DevOps = {"Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernates", "Linux"}

# adding the elements
DevOps.add("Jenkins")
print(DevOps)

# removing the elements
DevOps.remove("Linux")
print("Removing the Linux element")
print(DevOps)

# discard the elements - CICD elements is not there but discard won't display the error
DevOps.discard("CICD")
print(DevOps)

# removing the random element from the set
DevOps.pop()
print(DevOps)