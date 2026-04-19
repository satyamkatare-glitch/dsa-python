
# Question : Given an array , sort it using bubble sort.
# Time complexity = O(n^2)

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        isSwap = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                isSwap = True

        if not isSwap:
            break
        
    return arr
    
arr = [5,2,9,1,3]
sorted_arr = bubble_sort(arr)

print(sorted_arr)