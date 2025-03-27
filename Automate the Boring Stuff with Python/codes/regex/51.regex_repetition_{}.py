import re

message="hahaha i laugh a lot"
#usss group k repition ko find karna
ro=re.compile(r'(ha){3}')
mo=ro.search(message)
print(mo.group())