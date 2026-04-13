
# Question : Search target character in String.
# Time complexity : O(n)

def linear_search(str,target):
    for i in str:
        if i == target:
            return True
    return  False
           
        
str = "satyam katare"
target = "k"

found = linear_search(str,target)

print(found)