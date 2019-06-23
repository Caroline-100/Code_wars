def getCount(word):
    vowels = ['a','e','i','u','o','y']
    count = 0
    # print('letter', letter)
    for char in word:
        if char in vowels: 
            count += 1
    return count

print(getCount('abracadabra'))
assert( getCount("abracadabra")== 5)
assert( getCount("aeiuoy")== 6)
assert( getCount("trcgth")== 0)