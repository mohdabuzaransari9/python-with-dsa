import re

#see parenthesis in message
message = "batman batmobile batwomen"

#regex object
#use \( in pattern
#and or pipe symbol to define variations

#match only one of possible groups
ro=re.compile(r'bat(man|women|mobile)')

#match object
mo=ro.search(message)

if mo!=None:
    #None does not have a group method
    #you will get error
    print(mo.group(1))
