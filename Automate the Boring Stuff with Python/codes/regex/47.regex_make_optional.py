import re

#see parenthesis in message
message = "the adventure of batman"

#  ? defines 0 or more
#match only one of possible groups
ro=re.compile(r'bat(wo)?man')

#match object
mo=ro.search(message)

if mo!=None:
    #None does not have a group method
    #you will get error
    print(mo.group(0))


message = "the adventure of batwoman"

#match only one of possible groups
ro=re.compile(r'bat(wo)?man')

#match object
mo=ro.search(message)

if mo!=None:
    #None does not have a group method
    #you will get error
    print(mo.group(0))
