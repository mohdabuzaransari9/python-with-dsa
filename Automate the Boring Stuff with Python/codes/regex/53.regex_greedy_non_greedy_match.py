import re
message='123456789'

#greedy approach     
#means give priority to max number range     
ro=re.compile(r"(\d){3,5}")
mo=ro.search(message)
print("greedy approach - means give priority to max number range   ")
print(mo.group())


#putting question mark makes the {3,5}? to non greedy approach
#means give priority to less number

ro=re.compile(r"(\d){3,5}?")
mo=ro.search(message)
print("non greedy approach - means give priority to less number")
print(mo.group())
