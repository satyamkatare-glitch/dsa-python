
# Question : Count how many swaps bubble sort performs.
# Time complexity : O(n^2)

def bubble_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            temp = arr[j]
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = temp
                count += 1
                isSwap = True

        if not isSwap:
            break

    return count
        
arr = [4,3,2,1]

swaps_count = bubble_sort(arr)

print(swaps_count)