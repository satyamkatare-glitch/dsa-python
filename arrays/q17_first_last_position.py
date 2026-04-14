
# Question : Find first and last occurrence of target in sorted array.
# Time complexity = O(log n)

def findfirst(arr,target):

    low = 0
    high = len(arr) -1
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

def findlast(arr,target):

    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) //  2

        if arr[mid] ==  target:
            last = mid 
            low = mid + 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
        
    return last

arr = [1,2,2,2,2,2,3,4]
target = 2

first_occurence = findfirst(arr,target)
last_occurence = findlast(arr,target)

if first_occurence != -1 and last_occurence != -1:
    print(f"first occurrence = {first_occurence}\nlast occurence = {last_occurence}")
else:
    print("Target element not found")