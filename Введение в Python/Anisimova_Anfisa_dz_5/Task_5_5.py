src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = set()
num_repeat = set()
for num in src:
    if num not in num_repeat:
        result.add(num)
    else:
        result.discard(num)
    num_repeat.add(num)
result_ord = [num for num in src if num in result]
print(result_ord)

# ---------------------------------альтернативное решение--------------------------------------

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = {src[num] for num in range(len(src)) if src.count(src[num]) == 1}
result_ord = [num for num in src if num in result]

print(result_ord)
# --------------------------------------в одну строку------------------------------------------

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [num for num in src if src.count(num) == 1]

print(result)
