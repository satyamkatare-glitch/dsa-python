
# Question : Bubble sort in Desending Order.
# Time complexity = O(n^2)

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        isSwap = False

        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                isSwap = True

        if not isSwap:
            break
        
    return arr

arr = [3,1,4,2,0]
sorted_arr = bubble_sort(arr)

print(sorted_arr)