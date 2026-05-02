
# Question : Given a sorted array , find two numbers that add up to target.
# Time complexity : O(n)

def two_pointer(arr,target):

    low = 0
    high = len(arr) - 1

    while low < high :
        sum = arr[low] + arr[high]

        if sum == target:
            return arr[low],arr[high]
        
        elif sum > target:
            high -= 1

        else:
            low += 1

    return None

arr = [1,2,3,5,7,10,11,15]
target = 15

found = two_pointer(arr,target)

if found:
    print(found[0],found[1])
else:
    print("No pair found")