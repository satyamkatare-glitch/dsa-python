
# Question : Find target in rotated sorted array.
# Time Complexity : O(log n)

def binary_search(arr,target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = (low + high) // 2

        # target found
        if arr[mid] == target:
            return mid
        
        # left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # right half sorted       
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

arr = [4,5,6,7,0,1,2]
target = 0

found_index = binary_search(arr,target)

print(found_index) 