import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
f=s*((s-a)*(s-b)*(s-c))
d=(math.sqrt(f))
e="{:.2f}".format(d)
print(e)