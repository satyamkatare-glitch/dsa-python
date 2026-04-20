
# Question : Return array after k passes of bubble sort.
# Time complexity : O(k.n)

def bubble_sort(arr,k):
    n = len(arr)

    for i in range(k):
        isSwaps = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                isSwaps = True

        if not isSwaps:
            break
        
    return arr
                
arr = [5,1,4,2]
k = 2

k_passes = bubble_sort(arr,k)

print(k_passes)