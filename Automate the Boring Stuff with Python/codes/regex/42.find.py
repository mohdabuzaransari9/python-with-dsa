import re

message = "444-555-9999 and 444-555-0000"
#regex object
ro=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#match object
mo=ro.search(message)
#match object have a method called group
#to get the matched string
print(mo.group())