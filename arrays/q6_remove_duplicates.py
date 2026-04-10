
# Question : Remove duplicates from this array.
# Time complexity : O(n)

arr = [2,4,5,78,7,2,3,4,2,2,78] 

seen = set()
result = []

for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)