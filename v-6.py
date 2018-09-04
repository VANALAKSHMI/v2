#4
print("to check whether the input is  Alphabet or not")
x=(input("N="))
if(x.isalpha()==True):
    v=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for y in v:
        if(y==x):
            print("Alphabet")
            break
   
else:
      print("no ")
