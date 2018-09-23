#33
print("*****to count the spaces*****")
s=(input("enter your sentense:"))
if(len(s)<=1000):
   ch=s.split()
   cs=len(ch)-1
   print("space count:",cs)
else:
   print("invalid input")
