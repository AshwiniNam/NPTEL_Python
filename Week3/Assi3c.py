k=0
list_1=[]
for i in range(1,51):
    list_1.append(i)
a=int(input())
for i in list_1:
    if(i%a==0 and i!=a):
        k=k+1;
print(k)