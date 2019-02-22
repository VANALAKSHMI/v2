#73
n=int(input(""))
c=0
l=int(input(""))
a=0
r=int(input(""))
for x in range(l+1,r):
    if(n==x):
        c=c+1
if(c==1):
    print("yes")
else:
    print("no")
