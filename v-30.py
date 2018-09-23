#30
print("to print time")
print("enter the hour and minute in one by one")
print("enter your first hour and minute:")
h1= int(input("hour:"))
m1= int(input("minute:"))
h2= int(input("enter your second hour and minute; hour:"))
m2= int(input("minute:"))
h=h1-h2
m=m1-m2
if(m<0):
    he=h-1
    me=60+m
    print(he,":",me)
else:
    print(h,":",m)
