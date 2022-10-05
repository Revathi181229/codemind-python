import math
n=(input())
s=int(n)*int(n)
rs=n[::-1]
a=int(rs)*int(rs)
a=str(a)
b=a[::-1]
b="".join(b)
if s==int(b):
    print("True")
else:
    print("False")