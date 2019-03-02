#79
n=5
m=5
s=n*m
d=0
for i in range(1,s):
    a=i*i
    if(a==s):
        d=d+1
if(d==1):
    print("yes")
else:
    print("no")
