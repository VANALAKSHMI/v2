#9-FIND THE SUM OF THE FIRST K INTEGERS
print("FIND THE SUM OF THE FIRST K INTEGERS")
s=0
N=int(input("N="))
k=int(input("k="))
for x in range (1,N+1):
 print(x)
for x in range (1,k+1):
 s=s+x
print("output:",s)
