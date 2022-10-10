s=input()
n=int(input())
res=(s.count("a")*(n//len(s)))+(s[:n%len(s)].count("a"))
print(res)