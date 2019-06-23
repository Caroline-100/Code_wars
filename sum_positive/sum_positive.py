def positive_sum(arr):
    acc = 0
    for value in arr:
        # print(index)
        
        if (value >= 0):
            
            acc += value
    return acc

assert positive_sum([1,2,3,4,5]) == 15
assert positive_sum([1,-2,3,4,5]) == 13
assert positive_sum([-1,2,3,4,-5])==9
