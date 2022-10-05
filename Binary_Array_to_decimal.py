n=int(input())
l=list(map(int,input().split()))
op=""
def opt(op):
    return int(op,2)
for i in l:
    op=op+str(i)
print(opt(op))
