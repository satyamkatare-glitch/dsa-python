
# Question : Find the missing number.
# Time complexity : O(n)

arr = [1,2,4,5,6]

n = len(arr) + 1
total = n * (n + 1) // 2

print(total - sum(arr))