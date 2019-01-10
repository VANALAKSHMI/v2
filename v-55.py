#3
a=int(input(""))
c=0
if(a<=1000000000000):
 while a>0:
    re=a%10
    c=c+1
    a=a//10
print(c)
