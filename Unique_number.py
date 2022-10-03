n=list(input())
c=[]
for i in n:
    if i not in c:
        c.append(i)
if c==n:
    print("Unique Number")
else:
    print("Not Unique Number")
