def binary_search(arr,tgt):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if tgt==arr[mid]:
            return mid 
        if tgt>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6]
idx=binary_search(arr,8)
if idx ==-1:
    print("Number not found")
else:
    print("Number found at index:",idx)
        
        