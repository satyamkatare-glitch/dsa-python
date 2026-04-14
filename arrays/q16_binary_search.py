
# Question : Given a sorted array and target value , return the index of the target byusing binary search.
# Time complexity : O(log n)

def binary_search(arr,target):
    
    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1 

        else:
            high = mid - 1
    
    return -1

arr = [1,2,3,4,5]
target = 3

found = binary_search(arr,target)

if found != -1:
    print("Target Element found in index" , found)
else:
    print("Target element not found")