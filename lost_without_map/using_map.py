a = [1, 2, 3]
list2 = [4, 5, 6]


from operator import add
def maps(z):
    return map (add,z)

print(maps(a))