def sec_largest_ele(arr):
    arr.sort()
    if arr[-2] !=arr[-1]:
        return arr[-2]
        
arr = [2,3,865,351,1535,6245,45,634,57,52]

print(sec_largest_ele(arr))
