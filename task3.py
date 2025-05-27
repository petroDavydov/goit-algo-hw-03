# def hanoi(n, source, auxiliary, target, towers):
#     if n == 1:
#         disk = towers[source].pop()  # Забираємо диск з початкового стрижня
#         towers[target].append(disk)  # Кладемо його на цільовий стрижень
#         print(f"Перемістити диск {disk} з {source} на {target}")
#         print(f"Проміжний стан: {towers}")
#     else:
#         hanoi(n-1, source, target, auxiliary, towers)  # Переміщення n-1 дисків на допоміжний стрижень
#         hanoi(1, source, auxiliary, target, towers)  # Переміщення найбільшого диска на цільовий стрижень
#         hanoi(n-1, auxiliary, source, target, towers)  # Переміщення n-1 дисків на цільовий стрижень

# def solve_hanoi(n):
#     towers = {
#         'A': list(range(n, 0, -1)),  # Початковий стан: стрижень A заповнений дисками
#         'B': [],  # Допоміжний стрижень порожній
#         'C': []   # Цільовий стрижень порожній
#     }
#     print(f"Початковий стан: {towers}")

#     hanoi(n, 'A', 'B', 'C', towers)  # Виконання алгоритму переміщення

#     print(f"Кінцевий стан: {towers}")

# # Введення користувачем кількості дисків
# n = int(input("Введіть кількість дисків: "))
# solve_hanoi(n)