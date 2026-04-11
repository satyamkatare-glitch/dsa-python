
# Question : Check if element exists in Array.
# Time Complexity = O(n)

def linear_search(arr,target):
    for i in arr:
        if i == target:
            return True
    else:
        return False    
    
arr = [1,9,15,5,17,19]
target = 5

found = linear_search(arr,target)

print(f"Target found: {found}")