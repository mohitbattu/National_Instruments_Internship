def print_array(arr):
    for i in range(len(arr)):
        print(*arr[i])
def padding(arr,pad):
    output_array=arr[:]#copied
    for i in range(len(arr)):
        for j in range(pad):
            print(output_array[i].insert(j,0))#index #value
            print(output_array[i].append(0))
    for i in range(pad):
        output_array.insert(i,[0]*(len(arr[0])))
        output_array.append([0]*(len(arr[0])))
    return output_array
R,C=map(int,input("Enter range:\n").split())#n=R,m=C
matrix=[]#matrix
for i in range(R):
    b=[0]*C
    
    matrix.append(b)
for i in range(R):
    for j in range(C):
        matrix[i][j]=int(input("Enter Element at {0} {1}:\n".format(i+1,j+1)))
print(matrix)
pad=int(input("Enter padding:\n"))
matrix=padding(matrix,pad)
print_array(matrix)



