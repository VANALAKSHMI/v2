#1
x=(input(""))
if(x.isalpha()==False):
 n=int(x)
 if(n>0):
  print("Positive")
 elif(n<0):
  print("nagative")
 else:
  print("zero")
else:
 print("the input is invalid")
