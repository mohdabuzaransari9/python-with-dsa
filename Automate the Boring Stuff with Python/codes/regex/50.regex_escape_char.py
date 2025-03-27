import re

message="i learn to find ?*+\\n characters"
#  find ?*+\n characters
ro=re.compile(r'\?\*\+\\n')
mo=ro.search(message)
print(mo.group())