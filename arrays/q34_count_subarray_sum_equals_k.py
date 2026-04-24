
# Question : Count number of subarrays whose sum equal to k.
# Time complexity = O(n)

def prefix_sum(arr):

    ps_arry = [0] * len(arr)
    ps_arry[0] = arr[0]

    for i in range(1,len(arr)):
        ps_arry[i] = ps_arry[i-1] + arr[i]

    return ps_arry 

def count_sum(ps_arr,k):

    freq = {}
    count = 0

    for j in range(len(ps_arr)):

        if ps_arr[j] == k:
            count += 1
        
        if ps_arr[j] - k in ps_arr:
            count += freq[ps_arr[j] - k]

        freq[ps_arr[j]] = freq.get(ps_arr[j],0) + 1

    return freq,count

arr = [9, 4,0,20, 3, 10, 5]
k = 33

ps_arr = prefix_sum(arr)
count_subarray = count_sum(ps_arr,k)

print(count_subarray[0],count_subarray[1])
print(ps_arr)