number = int(input("Введіть кількість хвилин "))
hours, minutes = divmod(number, 60)

print(hours, "годин", minutes, "хвилин")