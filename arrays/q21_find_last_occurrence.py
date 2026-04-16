
# Question : Last occurrence using binary search.
# Time complexity : O(log n)

def find_last(arr,target):

    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return last

arr = [1,2,3,3,4,4,5,5,5,6]
target = 5

last_occcurence = find_last(arr,target)

if last_occcurence != -1:
    print(f"last occurence at index : {last_occcurence}")
else:
    print("Target not found")