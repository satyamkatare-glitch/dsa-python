
# Question : Explain and test stability of selection sort with duplicates.
# Time complexity : O(n^2)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def test_stability(arr):
    # Attach original indices
    arr_with_index = [(value, idx) for idx, value in enumerate(arr)]

    sorted_arr = selection_sort(arr_with_index)

    # Check stability
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i][0] == sorted_arr[i-1][0]:
            if sorted_arr[i][1] < sorted_arr[i-1][1]:
                return False  # order changed → unstable

    return True


arr = [2, 2, 1]

print(test_stability(arr))