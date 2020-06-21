def check(x):
    count=0
    for i in x:
        if max(i)>0:
            count=1
            break
    if count==1:
        return False
    else:
        return True
m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
cells=[]
for i in range(m):
    x=list(map(int,input().split(" ")))
    cells.append(x)
t=int(input("enter the number of sequences"))
for i in range(m):
    cells[i].append(0)
    cells[i]=[0]+cells[i]
cells.append([0]*(n+2))
cells=[[0]*(n+2)]+cells
m=m+2
n=n+2
for _ in range(t):
    new_cells=[[0]*(n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            new_cells[i][j]=cells[i][j]
    for i in range(m):
        for j in range(n):
            neighbours=[]
            neighbour_count=0
            if i-1>=0 and j-1<0:
                neighbours.append([i-1,j])
            elif i-1<0 and j-1>=0:
                neighbours.append([i,j-1])
            elif i-1>=0 and j-1>=0:
                neighbours.append([i-1,j])
                neighbours.append([i,j-1])
                neighbours.append([i-1,j-1])
            else:
                neighbours=neighbours[:]
            if i+1<=m-1 and j+1>n-1:
                neighbours.append([i+1,j])
            elif i+1>m-1 and j+1<=n-1:
                neighbours.append([i,j+1])
            elif i+1<=m-1 and j+1<=n-1:
                neighbours.append([i+1,j])
                neighbours.append([i,j+1])
                neighbours.append([i+1,j+1])
            if i-1>=0 and j+1<=n-1:
                neighbours.append([i-1,j+1])
            if i+1<=m-1 and j-1>=0:
                neighbours.append([i+1,j-1])
            for k in neighbours:
                p=k[0]
                q=k[1]
                if cells[p][q]==1:
                    neighbour_count+=1
            if cells[i][j]==1:
                if neighbour_count>3 or neighbour_count<2:
                    new_cells[i][j]=0
            else:
                if neighbour_count==3:
                    new_cells[i][j]=1
    for i in range(m):
        for j in range(n):
            cells[i][j]=new_cells[i][j]
    for i in range(m):
        cells[i].append(0)
        cells[i]=[0]+cells[i]
    cells.append([0]*(n+2))
    cells=[[0]*(n+2)]+cells
    m=m+2
    n=n+2
    print(_+1)
    print(cells)

                
                    

    
            
                        
                
    
