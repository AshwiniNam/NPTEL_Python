l=[]
for i in range(1,51):
    l.append(i)
a,b=input().split()
a=int(a)
b=int(b)
x=l[a:b]

for i in x:
    print(i)