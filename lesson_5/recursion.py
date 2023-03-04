# Задача 1. Есть число N, вывести последовательность от N до 1 включительно
def rec(n):
    if n > 1:
        print(n, end=" ")
        rec(n - 1)


rec(int(input("Введите число n: ")))


# ======================================================================
# Задача 2. Функция факториала числа Рекурсия.

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

n = int(input("\nВведите число для вычисления факториала: "))
print(f'Факториал числа {n} = {fac(n)}')
# ======================================================================
# Факториал числа цикл   while
n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
# ======================================================================

# Факториал числа цикл   for
n = int(input())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)
# ======================================================================

# Fibonachi recursion
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f'Фибоначи рекурсия: {fibonacci(10)}')


# ======================================================================

# Задача 2. Функция Fibonachi.

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# ======================================================================
# Fibonachi cycle while
fib1 = fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1

print("Значение этого элемента:", fib2)

# ======================================================================
# Fibonachi cycle for
fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')



# ======================================================================
print(f'\n')
# Быстрая сортировка. Рекурсия.
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2]))

# ======================================================================
# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list_1)
print(list_1)