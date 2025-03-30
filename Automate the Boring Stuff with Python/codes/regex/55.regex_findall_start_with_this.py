import re
message="python is my expertise"
# ^ this denotes string start with this pattern
ro=re.compile(r"^python")
mylist=ro.findall(message)

#findall does not return match object
print(mylist)