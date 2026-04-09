
# Question : Count even and odd number and count how many even or odd are there.
# Time Compelexity : O(n)

arr = [1,22,35,55,36,78,2,34]

even = odd = 0

# For even numbers 
print("Your even numbers are :- ")

for i in arr:
    if i % 2 == 0:
        print(i)
        even += 1

print(f"Total even number is : {even} \n")

# For odd numbers 
print("Your odd number are :- ")

for i in arr:
    if i % 2 != 0:
        print(i)
        odd += 1

print(f"Total odd number is : {odd}")