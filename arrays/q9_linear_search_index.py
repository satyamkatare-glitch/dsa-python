
# Question : Find Index of an Target element
# Time complexity : O(n)

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10,50,30,40,60]
Target = 30

found = linear_search(arr,Target)

if found != -1:
    print(f"Target found at index {found}")
else:
    print("Target not found")