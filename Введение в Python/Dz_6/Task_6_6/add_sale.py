import sys

_sale = sys.argv[1].replace(".", "")
if _sale.isdigit():
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(f'{sys.argv[1]}\n')
else:
    sys.exit("Необходимо было ввести число")


