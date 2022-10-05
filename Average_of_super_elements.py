n=int(input())
l=list(map(int,input().split()))
d=[]
s=0
for i in l:
    if l.count(i)==i:
        s=1
        if i in d:
            continue
        d.append(i)
if s==0:
    print("-1")
else:
    avg=(sum(d))/(len(d))
    e="{:.2f}".format(avg)
    print(e)