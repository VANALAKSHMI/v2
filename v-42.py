#32
print("*****to count the words*****")
s=(input("enter your sentense:"))
if(len(s)<=1000):
   ch=s.split()
   cs=len(ch)
   print("word count:",cs)
else:
   print("invalid input")
