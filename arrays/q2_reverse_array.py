
# Question : Reverse an array
# Time complexity = O(n)

arr = [1,2,3,4,5,6]

left = 0
right = len(arr) - 1

while left < right:
    arr[left],arr[right] = arr[right],arr[left]
   
    left += 1
    right -= 1

print()