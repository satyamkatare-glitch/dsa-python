
# Question : Find maximum and minimum in an Array
# Time complexity : O(n)

arr = [6,10,12,32,4,5,2]

max_value = arr[0]
max_index = 0

min_value = arr[0]
min_index = 0

for i in range(len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i 
    else:
        min_value = arr[i]
        min_index = i

print(f"Your max value is {max_value} at {max_index} index\nYour min value is {min_value} at {min_index} index")
        



