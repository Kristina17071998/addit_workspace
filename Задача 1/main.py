# Считываем количество чисел
n = int(input("Введите количество чисел: "))

# Считываем и сразу сортируем числа в обратном порядке
numbers = sorted([float(input("Введите число: ")) for _ in range(n)], reverse=True)

# Выводим отсортированные числа
print("Отсортированные числа в обратном порядке:", *numbers, sep='\n')
