
import re
x = input("")
n = re.sub('[\w]' ,'', x)
print(len(n))
