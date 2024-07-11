immutable_var = (1, 2, 3, 'BUBA', True)
print(immutable_var)
# immutable_var[0] = 1
# print(immutable_var) # не работает, т.к это кортеж (не изменяемый список)

mutable_list = [1, 2, 3, 'BUBA', True]
print(mutable_list)
mutable_list[4] = False
print(mutable_list)