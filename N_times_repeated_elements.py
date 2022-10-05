n=int(input())
l=list(map(int,input().split()))
x=int(input())
c=[]
d=[]
s=0
for i in l:
    if l.count(i)==x:
        c.append(i)
for j in c:
    if j not in d:
        d.append(j)
        s=1
if s==0:
    print("-1")
else:
    print(*d)