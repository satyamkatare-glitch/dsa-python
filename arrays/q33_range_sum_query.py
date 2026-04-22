
# Question : Given array and queries (l,r) , find sum from index l to r.
# Time complexity : O(1)

def prefix_sum(arr,query):

    if not arr:
        return 0

    ps_arr = []
    ps_arr.append(arr[0])
 
    for i in range(1,len(arr)):
        ps_arr.append(ps_arr[i-1] + arr[i])

    return ps_arr

def range_sum(prefix_sum,l,r):
    if l == 0:
        return prefix_sum[r]
    return prefix_sum[r] - prefix_sum[l-1]

arr = [1,2,3,4,5]
query = (1,3)

ps_array = prefix_sum(arr,query)
result = range_sum(ps_array,query[0],query[1])

print(result)