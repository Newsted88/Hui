# Порівняння відповідає True (так) або False (ні).
money = 50
price = 40
print(money == price)  # False: два знаки = перевіряють рівність.
print(money != price)  # True: значення різні.
print(money > price)  # True: 50 більше за 40.
print(money < price)  # False: 50 не менше за 40.
print(money >= price)  # True: грошей вистачає, навіть якщо сума дорівнює ціні.
print(money <= price)  # False: 50 не менше і не дорівнює 40.
has_ticket = True
print(money >= price and has_ticket)  # True лише коли обидві умови істинні.
print(money < price or has_ticket)  # True, бо хоча б одна умова істинна.
print(not has_ticket)  # False: not змінює логічне значення.
# Помилка: один знак = не перевіряє рівність.
