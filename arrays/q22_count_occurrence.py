
# Question : Count occurences using Binary search.
# Time complexity : O(log n)

def first_occurrence(arr,target):

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

def last_occurrence(arr,target):
    
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

def count(arr,target):
    
    first = first_occurrence(arr,target)
    if first == -1:
        return 0
    
    last = last_occurrence(arr,target)


    # Calculate count occurrences
    count = last - first + 1

    return count

arr = [1,2,2,3,3,4,4,4,5,5,5,5,6,6,6,7]
target = 6

count_occurrences = count(arr,target)

if count_occurrences != 0:
    print(f"Count of {target} is:", count(arr, target))
else:
    print("Target not found")