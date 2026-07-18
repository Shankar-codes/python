# list example
DevOps = ["Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernetes", "Python"]

# Accessing the list
print(DevOps[3])
print(DevOps[6])

# Adding the elements in the list at last
DevOps.append("Jenkins")
print(DevOps)

# Adding the elements in the specific index using insert
DevOps.insert(0, "ArgoCD")
print(DevOps)
