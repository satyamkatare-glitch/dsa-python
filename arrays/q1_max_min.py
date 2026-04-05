
 # Question : Find maximum and minimum in an Array

arr = [3,7,9,2,1]

max_value  = arr[0]
min_value = arr[0]

for num in arr:
    if num > max_value:
        max_value = num
    else:
        min_value = num

print(max_value,min_value)
