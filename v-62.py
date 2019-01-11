a=int(input(""))
re=0
while(a>0):
    r=a%10
    re=re*10+r
    a=a//10

while(re%10):
    if(re==1):
        print("one")
        break
    if(re==2):
        print("two")
        break
    if(re==3):
        print("three")
        break
    if(re==4):
        print("four")
        break
    if(re==5):
        print("five")
        break
    if(re==6):
        print("six")
        break
      if(re==7):
        print("seven")
        break
    if(re==8):
        print("eight")
        break
    if(re==9):
        print("nine")
        break
     if(re==10):
        print("ten")
        break
    re=re//10    
        
        
        
