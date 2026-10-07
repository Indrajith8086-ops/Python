n=2
arr=[1,2,3,4,5]
l=len(arr)
for i in range(n):
    first=arr[0]
    for i in range(l-1):
        arr[i]=arr[i+1]
        
    arr[l-1]=first
print(arr)
