#17-TO CHECK WHETHER A NUMBER IS ARMSTRONG OR NOT
print("TO CHECK WHETHER A NUMBER IS ARMSTRONG OR NOT")
n=int(input("N="))
if(n<=100000):
    t=n
    s=0
    a=0
    while n>0:
        re=n%10
        a=re**3
        s=s+a
        n=n//10

    if(t==s):
        print("armstrong")
    else:
        print("not armstrong")
else:
     print("invalid input")
