DevOps = ["Linux", "Shell", "Ansible", "Terraform", "Docker", "Kubernetes", "Python"]
i=1
for skills in DevOps:
    if skills=="Docker":
        break
    print(i, skills)
    i+=1
    
print("------------continue example -----------")
j=1
for skill in DevOps:
    if skill=="Docker":
        continue
    print(j, skill)
    j+=1