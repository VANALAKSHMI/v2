#66
N=int(input(""))
flag=0
for x in range (1,N+1) :
    if(N%x==0):
        flag=flag+1
if(flag==2):
        print("Yes")
else:
        print("no")
