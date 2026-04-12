
# Question : Find last occurrence of target value.
# Time complexity : O(n)

def linear_search(arr,target):
    
    index = -1

    for i in range(len(arr)):
        if arr[i] == target:
            index = i

    return index

arr = [2,4,1,2,15,6,2,9,13]
target = 2

last_occurrence = linear_search(arr,target)

if last_occurrence != -1:
    print(f"Last occurrence index: {last_occurrence}")
else:
     print("Target not found")