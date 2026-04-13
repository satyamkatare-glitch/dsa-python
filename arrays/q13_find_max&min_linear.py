
# Question : Find maximum and minimum element using linear search.
# Time complexity : O(n)

def linear_search(arr):

    max_value = arr[0]
    min_value = arr[0]

    for i in arr:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
    
    return max_value,min_value

arr = [2,45,56,78,92,52,98,1,2,5]

found = linear_search(arr)

print("Maximum:", found[0])
print("Minimum:", found[1])