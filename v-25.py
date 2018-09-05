#15-DISPLAY EVEN NUMBERS BETWEEN 2 INTERVALS
print("DISPLAY EVEN NUMBERS BETWEEN 2 INTERVALS")
s=int(input("s="))
e=int(input("e="))
for x in range(s+1,e):
    if(x%2==0):
        print(x)
