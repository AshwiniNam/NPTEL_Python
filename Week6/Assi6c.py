n=int(input())
m=[]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    m.append(l)

for i in range(n):
    for j in range(n):
        if(i>=j):
            if(j==n-1):
                print(m[i][j],end="")
            else:
                print(m[i][j], end=" ")
        else:
            if (j == n - 1):
                print(0, end="")
            else:
                print(0, end=" ")
    if(i!=n-1):
        print()