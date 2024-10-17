def linear_search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1

arr = [2,3,865,351,1535,6245,45,634,57,52]
n=len(arr)
x=634
print(linear_search(arr,n,x))

