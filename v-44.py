
#34
print("*****to count the lines*****")
s=(input("enter your paragraph:"))
if(len(s)<=1000):
   ch=s.split(".")
   cs=len(ch)
   print("line count:",cs)
else:
   print("invalid input")
