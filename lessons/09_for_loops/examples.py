# for бере наступне значення з range і виконує блок з відступом.
for number in range(3):
    print(number)  # Побачимо 0, 1, 2; верхня межа 3 не входить.
for number in range(1, 4):
    print(number)  # Побачимо 1, 2, 3.
for number in range(2, 7, 2):
    print(number)  # Побачимо 2, 4, 6; третє число задає крок.
for letter in "кіт":
    print(letter)  # Побачимо три літери на окремих рядках.
# На відміну від while, тут не потрібно самому збільшувати number.
# Помилка: range(1, 5) не включить 5.
