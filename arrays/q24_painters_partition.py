
# Question : Given boards and painters , assign boards (continuous) , such that maximum time taken by any painter is minimized.
# Time complexity : O(n log n)

def isPossible(boards,painters,maxTime):

    count = 1
    time = 0

    for board in boards:

        if board > maxTime:
            return False
        
        if board + time <= maxTime:
            time += board
        else:
            count += 1
            time = board
            if count > painters:
                return False
    return True
        
def painterPartition(boards,painters):

    if len(boards) < painters:
        return -1
    
    left = max(boards) 
    right = sum(boards) 
    ans = right

    while left <= right:

        mid = (left + right) // 2

        if isPossible(boards,painters,mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

boards = [10,20,30,40,50]
painters = 2

result = painterPartition(boards,painters)

if result == -1:
    print("Painter allocation not possible")
else:
    print(f"Minimum maximum time assigned to a painter: {result}")