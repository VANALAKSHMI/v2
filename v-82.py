#72
s=(input(""))
l=['a','e','i','o','u']
c=0
for x in range(len(s)):
    for i in range(0,5):
        if(s[x]==l[i]):
            c=c+1
if(c>0):
    print("yes")
else:
    print("no")
