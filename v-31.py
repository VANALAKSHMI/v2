#21
print("to find arithmatic progression")
n=int (input("N="))
a=int(input("A="))
d=int(input("D="))
if(1<n,a,d<100000):
 i=0
 s=0
 while (i<n):
   s=s+a
   a=a+d
   i=i+1
 print("sum:",s)
else:
 print("the input is invalid")
