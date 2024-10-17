def largest_ele(arr,n,max):
    for i in range(0,n):
        if arr[i]>max:
            max=arr[i]
    return max
    

arr = [2,3,865,351,1535,6245,45,634,57,52]
n=len(arr)
max = arr[0]

print(largest_ele(arr,n,max))
