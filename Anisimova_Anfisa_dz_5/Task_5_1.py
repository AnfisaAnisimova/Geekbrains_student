def odd_num_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = odd_num_gen(34)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(*nums_gen)
