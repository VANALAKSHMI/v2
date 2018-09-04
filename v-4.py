#2
print("to check whether the input is odd or even")
x=(input("N="))
if(x.isalpha()==False):
    n=int(x)
    if(n<0):
         print("the input is invalid")
    else:
        if(n%2==0):
            print("even")
        else:
            print("odd")
else:
 print("the input is invalid")
