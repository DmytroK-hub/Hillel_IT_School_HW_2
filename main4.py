price = int(input("Введіть ціну товару: "))
discount = int(input("Введіть знижку: "))

solution = price * (discount / 100)
final_price = price - solution

print(final_price)