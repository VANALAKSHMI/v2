#28
print("to print element with an index ")
n=int(input("N="))
l=[]
print("enter your ",n,"integers")
for x in range(0,n):
        a=int(input(""))
        l.append(a)
for x in range(0, n):
    print(l[x],x)
