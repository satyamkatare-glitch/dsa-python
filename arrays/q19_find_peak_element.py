
# Question : Return index of any peak element.
# Time complexity : O(log n)

def binary_search(arr):
    
    low = 0
    high = len(arr) - 1 

    while low < high:

        mid = (low + high) // 2

        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid 
    
    return low,high

arr = [1,2,3,1]

found = binary_search(arr)

print(found)