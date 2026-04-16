
# Question : Find first occurence using binary search.
# Time complexity = O(log n)

def find_first(arr,target):

    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid -1

    return first

arr = [1,2,3,3,3,4,4,4,5,5,5,6]
target = 5

first_occurence = find_first(arr,target)

if first_occurence != -1:
    print(f"first occurence at index : {first_occurence}")
else:
    print("Target not found")