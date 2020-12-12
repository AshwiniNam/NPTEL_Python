n=int(input())
for i in range(0,n):
    num=1
    for j in range(0,i+1):
        if(j==n-1):
            print(num, end="")
        else:
            print(num, end=" ")
            num=num+1
    if(i!=n-1):
        print()