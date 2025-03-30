import re
message="i love python ,python is my expertise"
ro=re.compile(r"python")
mylist=ro.findall(message)

#findall does not return match object
print(mylist)