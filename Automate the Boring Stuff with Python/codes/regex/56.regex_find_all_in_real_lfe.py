
#findall pattern inreal lifetext

message="12 drums 10 pipes 15 Covers and nothing"

import re

ro=re.compile("\d+\s\w+")

mylist=ro.findall(message)

print(mylist)