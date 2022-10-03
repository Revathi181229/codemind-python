n=int(input())
x=abs(n)
f=len(str(x))-1
a=10**f
s=0
for i in range(len(str(x))):
    r=x%10
    r=r*a
    s+=r
    x//=10
    a//=10
if n<0:
    print("-"+str(s))
else:
    print(s)