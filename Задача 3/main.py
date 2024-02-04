# Read the number of elements in the list
N = int(input())

# Read the numbers into a list
numbers = [int(input()) for _ in range(N)]

# Read the starting and ending indices for summation
print("Введите начальный и конечный индексы элементов для суммирования:")

p = int(input("Начальный индекс (1 ≤ p ≤ N): "))
q = int(input("Конечный индекс (p ≤ q ≤ N): "))

# Output the sum of elements in the specified range
sum_of_range = sum(numbers[p-1:q])
print(f"Сумма элементов в заданном диапазоне: {sum_of_range}")