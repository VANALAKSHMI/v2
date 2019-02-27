#79
n=int(input(""))
m=int(input(""))
s=n*m
c=0
for x in range(1,s):
    a=x*x
    if(a==s):
        c=c+1
if(c==1):
    print("yes")
else:
    print("no")
