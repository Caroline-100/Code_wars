def stringy (size):
    ans = ""
    for nb in range(size):
        if nb % 2 == 0:
            ans += "1"
        else:
            ans += "0"
    return ans




assert stringy(3) == '101'
assert stringy(5) == '10101'
assert stringy(12) == '101010101010'
assert stringy(26) == '10101010101010101010101010'
assert stringy(28) == '1010101010101010101010101010'