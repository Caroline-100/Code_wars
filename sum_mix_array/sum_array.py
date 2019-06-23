a = [9, 3, '7', '3']
# nb_int =[]
# zero = 0
# for num in a:
#     nb_int.append(int(num))
# for number in nb_int:
#     zero += number
#     # print(zero)
# # print(number)

# print(num[0:1])
def sum_mix(arr):
    nb_int =[]
    sum_of_number = 0
    for num in arr:
        nb_int.append(int(num))
    for number in nb_int:
        sum_of_number += number
    return sum_of_number

print(sum_mix(a))





assert sum_mix([9, 3, '7', '3']) == 22
assert sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])==42
assert sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])==41
assert sum_mix(['1', '5', '8', 8, 9, 9, 2, '3'])== 45
assert sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])== 61