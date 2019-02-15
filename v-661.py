#56
a=(input(""))
c=0
if(len(a)<=1000):
    for x in a:
        if(x.isdigit()==True):
            c=c+1
if(c>=1):
    print("Yes")
else:
    print("No")
