
# Question : Sort an array using slection sort.
# Time complexity : O(n^2)
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        # swap AFTER finding the minimum
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 255, 25, 12, 22, 11]

sorted_arr = selection_sort(arr)

print(sorted_arr)