
# Question : Allocate books to students such that the maximum pages assigned to a student is minimum. Each student get continuous books.
# Time complexity : O(n log n)

def isPossible(books,students,maxPages):
    st = 1
    pages = 0

    for book in books:

        if book > maxPages:
            return False
        
        if pages + book <= maxPages:
            pages += book
        else:
            st += 1
            pages = book
            if st > students:
                return False
    return True

def allocateBooks(books,students):

    left = max(books)
    right = sum(books)
    ans = -1

    while left <= right:

        if students > len(books):   
            return -1

        mid = (left + right) // 2

        if isPossible(books,students,mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

books  = [10,20,30,40]
students = 2

result =  allocateBooks(books,students)

if result == -1:
    print("Allocation not possible")
else:
    print(f"Minimum maximum pages assigned: {result}")