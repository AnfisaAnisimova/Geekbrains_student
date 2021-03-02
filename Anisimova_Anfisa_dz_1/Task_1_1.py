duration = int(input("Введите количество секунд: "))

seconds = duration % 60
minutes = duration // 60
hours = duration // 3600
days = duration // 86400

print("До минуты:", minutes, "минут", seconds, "секунд")
print("До часа:", hours, "часов", minutes % 60, "минут", seconds, "секунд")
print("До суток:", days, "суток", hours % 24, "часов", minutes % 60, "минут", seconds, "секунд")
