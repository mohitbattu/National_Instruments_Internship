m,n=map(int,input().split())
arr=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j]=i*j
print(arr)
