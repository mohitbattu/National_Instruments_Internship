output=[]
for i in range(1000,3000):
    count=0
    t=i
    for j in range(4):
        r=i%10
        i=i//10
        if r%2==1:
            count=1
            break
    if count==0:
        output.append(t)
print(output)
    
    
