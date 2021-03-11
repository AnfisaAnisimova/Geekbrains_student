n = int(input("Введите число: "))

nums_gen = (num for num in range(1, n + 1, 2))
print(*nums_gen, sep=", ")
