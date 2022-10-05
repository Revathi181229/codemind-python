n=(input())
p=1
s=0
for i in n:
    s+=int(i)**p
    p+=1
if str(s)==n:
    print("True")
else:
    print("False")