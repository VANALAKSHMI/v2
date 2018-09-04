#3
print("to check whether the input is  vowel or not")
x=input("enter your value:")
if(x.isalpha()==True):
    v=["a","e","i","o","u"]
    for y in v:
        if(y==x):
            print("vowel")
            break
    else:
            print("consonent")
else:
     print("invalid")
