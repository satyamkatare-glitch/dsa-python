
# Question : Character frequency Count.
# Time complexity : O(n)

def char_frequency(str):

    freq = {}

    for i in str:
        freq[i] = freq.get(i,0) + 1
     
    return freq


str = "banana"

frequency_count = char_frequency(str)

print(frequency_count)