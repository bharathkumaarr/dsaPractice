def sec_largest_ele(arr):
    
    largest = -1
    sec_largest = -1
    
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    for j in range(0,len(arr)):
        if arr[j]>sec_largest and arr[j]!=largest:
            sec_largest=arr[j]
    return sec_largest
        
arr = [2,3,865,351,1535,6245,45,634,57,52]

print(sec_largest_ele(arr))
