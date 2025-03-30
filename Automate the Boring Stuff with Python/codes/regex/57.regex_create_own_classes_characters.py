

message="hello FRIEND,"

import re
mo=re.findall(pattern=r"[a-zA-z]",string=message)
#there is no ,
#save each character in list as a item
print(mo)