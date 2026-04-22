
# Question : Given an array , create a prefix sum array.
# Time complexity : O(n)

def prefix_sum(arr):

    if not arr:
        return []

    ps_arr = []
    ps_arr.append(arr[0])

    for i in range(1,len(arr)):
        ps_arr.append(ps_arr[i-1] + arr[i])

    return ps_arr

arr = [1,2,3,4]

ps_array = prefix_sum(arr)

print(ps_array)