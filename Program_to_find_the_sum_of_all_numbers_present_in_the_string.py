n=input()
s=0
for i in n:
    if i.isnumeric():
        s+=int(i)
print(s)