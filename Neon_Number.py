n=int(input())
x=n*n
sum=0
while x:
    r=x%10
    sum=sum+r
    x=x//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")