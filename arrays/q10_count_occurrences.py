
# Question : Count occurrences of Element
# Time complexity : O(n)

def linear_search(arr,target):

    count = 0

    for i in arr:
        if i == target:
            count += 1

    return count


arr = [7,4,5,7,1,6,3,7]
target = 7

occurrence = linear_search(arr,target)

if occurrence > 0:
    print(f"Total occurrences of {target}: {occurrence}")
else:
     print("Target not found")