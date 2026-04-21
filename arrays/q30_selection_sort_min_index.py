
# Question : Print index of minimum element found in each pass.
# Time complexity : O(n^2)

def selection_sort(arr):
    n = len(arr)
    arr_mid = []

    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr_mid.append(min_index)

        # swap
        arr[min_index] , arr[i] = arr[i] , arr[min_index]
    
    return arr_mid

arr = [5,2,8,1]

min_indices = selection_sort(arr)

print("Sorted array:", arr)
print("Min indices per pass:", min_indices)