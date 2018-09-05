#14-DISPLAY ODD NUMBERS BETWEEN 2 INTERVALS
print("DISPLAY ODD NUMBERS BETWEEN 2 INTERVALS")
s=int(input("s="))
e=int(input("e="))
if(s<=100000)&(e<=10000):
    for x in range(s,e+1):
     if(x%2!=0):
        print(x)

else:
    print("input is invalid")
