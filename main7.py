number = int(input("Введіть 4-x значне число: "))

thousand, remaining = divmod(number, 1000)
one_hundred, shortage = divmod(remaining, 100)
ten, one = divmod(shortage, 10)

print(thousand)
print(one_hundred)
print(ten)
print(one)