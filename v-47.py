#37
print("*****to swap two numbers*****")
a=int(input("first number:"))
b=int(input("second number:"))
t=0
if(a,b<=100000):
    t=a
    a=b
    b=t
    print("after swaping:",a,b)
else:
   print("invalid input")
