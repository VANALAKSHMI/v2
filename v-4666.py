#6
s=(input("string:"))
i=len(s)-1
rev=""
c=0
d=0
f=0
while(i>=0):
       
        if(s[i].isnumeric()==False):
            d=d+1
        if(s[i].isalpha()==True):
            f=f+1
        k=d-f
        i=i-1
print(k)
