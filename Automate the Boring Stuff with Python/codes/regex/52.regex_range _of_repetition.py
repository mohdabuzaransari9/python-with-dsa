import re
message="hello hahahahaha"
#definng range min 3 baar max 5 baar
ro=re.compile(r"(ha){3,5}")
mo=ro.search(message)
print(mo.group())


#also can do slicing by using ,