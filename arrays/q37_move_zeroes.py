
# Question : Move all zeroes to end while maintaining order.
# Time complexity : O(n)

def move_zeroes(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1

    return arr

arr = [0,1,0,3,12]
new_arr = move_zeroes(arr)

print(new_arr)