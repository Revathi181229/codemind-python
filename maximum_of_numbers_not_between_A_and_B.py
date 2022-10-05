n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
s=0
for i in l:
    if a>i or b<i:
        d.append(i)
        s=1
if(s==0):
    print("-1")
else:
    print(max(d))
    