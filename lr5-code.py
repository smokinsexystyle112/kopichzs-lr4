def check_column(column):
    """Проверка, содержит ли столбец только неположительные элементы."""
    return all(value <= 0 for value in column)

def count_negative_columns(matrix):
    """Подсчет количества столбцов, содержащих только неположительные элементы."""
    return sum(1 for col in range(len(matrix[0])) if check_column([matrix[row][col] for row in range(len(matrix))]))

# Ввод двумерных массивов для тестирования
matrix_a = [
    [-1, 2, -3],
    [-4, -5, -6],
    [-7, 8, -9]
]

matrix_b = [
    [0, 1, -2],
    [-3, -4, -5],
    [-6, 7, 8]
]

# Подсчет столбцов с неположительными элементами в каждом массиве
count_a = count_negative_columns(matrix_a)
count_b = count_negative_columns(matrix_b)

# Вывод результата
if count_a == 0 and count_b == 0:
    print("Нет столбцов, содержащих только неположительные элементы в обоих массивах.")
else:
    print(f"Массив A: количество столбцов с неположительными элементами = {count_a}")
    print(f"Массив B: количество столбцов с неположительными элементами = {count_b}")