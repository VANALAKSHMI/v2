
#31
print("*****to count the character*****")
s=(input("enter your character:"))
c=0
for x in range(len(s)):
   c=c+1
ch=s.split()
cs=len(ch)
cn=c-(cs-1)
print("character count:",cn)
