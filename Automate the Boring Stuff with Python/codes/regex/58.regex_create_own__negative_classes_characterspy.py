

message="hello FRIEND"

import re
mo=re.findall(pattern=r"[^A-Z]",string=message)
#there is no ,
#save each character in list as a item
print(mo)