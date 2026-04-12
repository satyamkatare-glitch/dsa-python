
# Question : Find all indices of target element.
# Time complexity : O(n)

def linear_search(arr,target):

    index = []

    for i in range(len(arr)):
        if arr[i] == target:
            index.append(i)

    return index



arr = [1,2,34,45,2,3,4,2,1,35]
target = 2

indices = linear_search(arr,target)

if indices:
    print("Target found at indices:", indices)
else:
    print("Target not found")