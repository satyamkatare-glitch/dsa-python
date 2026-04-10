
# Question : Find second largest element in this array.
# Time complexity : O(n)

arr = [12,78,32,450,564,22,334,246,342,450]

largest = float('-inf')
sec_largest = float('-inf')
largest_index = sec_largest_index = 0

for i in range(len(arr)):
    if arr[i] > largest:
        sec_largest = largest
        sec_largest_index = largest_index

        largest = arr[i]
        largest_index = i
    
    elif arr[i] > sec_largest and arr[i] != largest:
        sec_largest = arr[i]
        sec_largest_index =  i

print(f"Your second largest element is {sec_largest} at {sec_largest_index} index")