import re

message = "444-555-9999 and 444-555-0000"

#regex object
#use parenthesis to provide groups
ro=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#match object
mo=ro.search(message)

print(mo)

#0th group contain whole thing
print(mo.group(0))

#1st group contain 1st group
print(mo.group(1))

#2nd group contain 2nd group
print(mo.group(2))