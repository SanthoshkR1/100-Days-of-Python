def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr=arr[i]
        j=i-1
        while j>=0 and curr < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=curr 
arr=[4,5,1,3,2,6]
insertion_sort(arr)
print(arr)