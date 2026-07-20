# list example
DevOps = ["Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernetes", "Python"]

# Accessing the list
print(DevOps[3])
print(DevOps[6])

# Adding the elements in the list at last
DevOps.append("Jenkins")
print(DevOps)

# extend the elements
DevOps.extend(["GitHub Actions", "Promethesys"])
# Adding the elements in the specific index using insert
DevOps.insert(0, "ArgoCD")
print(DevOps)

# Removing the elements
DevOps.remove("ArgoCD")
print(DevOps)

# Removing the elements at specific index or removing the last element
DevOps.pop()
print(DevOps)

DevOps.pop(0)
print(DevOps)

DevOps_1=DevOps.copy()
DevOps_1.remove("Jenkins")
print(f"printing the shallow copy {DevOps_1}.")