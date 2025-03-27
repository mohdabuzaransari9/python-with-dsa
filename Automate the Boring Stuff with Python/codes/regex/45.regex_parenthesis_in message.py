import re

#see parenthesis in message
message = "(444)-555-9999 and (444)-555-0000"

#regex object
#use \( in pattern
ro=re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')

#match object
mo=ro.search(message)

print(mo.group())
