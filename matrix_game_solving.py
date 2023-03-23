import random
import pandas as pd
import matplotlib.pyplot as plt


# Упрощение платёжной матрицы
def simplifying(matrix):
    minimum = min([min(row) for row in matrix])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += abs(minimum)

    # Удалить
    print('Початкова платіжна матриця: ')
    print(pd.DataFrame(matrix, index=[f'A{i + 1}' for i in range(len(matrix))],
                       columns=[f'B{i + 1}' for i in range(len(matrix[0]))]))

    # Удаляем пассивные стратегии игрока А
    new_matrix = matrix.copy()
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            if i == k:
                continue
            flag = True
            for j in range(len(matrix[0])):
                if matrix[k][j] < matrix[i][j]:
                    flag = False
            if flag:
                if matrix[i] in new_matrix:
                    new_matrix.remove(matrix[i])

    print()
    print(pd.DataFrame(new_matrix, index=[f'A{i + 1}' for i in range(len(new_matrix))],
                       columns=[f'B{i + 1}' for i in range(len(new_matrix[0]))]))

    # Удаляем пассивные стратегии игрока В
    # final_matrix = new_matrix.copy()
    # for i in range(len(new_matrix[0])):
    #     for j in range(len(new_matrix[0])):
    #         if i == j:
    #             continue
    #         else:
    #             flag = True
    #             for k in range(len(new_matrix)):
    #                 if new_matrix[k][i] < new_matrix[k][j]:
    #                     flag = False
    #             if flag:
    #                 for row in new_matrix:
    #                     row.pop(j)
    #
    # print()
    # print(pd.DataFrame(final_matrix, index=[f'A{i + 1}' for i in range(len(final_matrix))],
    #                    columns=[f'B{i + 1}' for i in range(len(final_matrix[0]))]))

    return new_matrix


# Упрощение платёжной матрицы к виду 2 x n
def two_x_n(matrix):
    simplified_matrix = [matrix[-1], matrix[-2]]
    print('Спрощена платіжна матриця:\n')
    return simplified_matrix


# Аналитический метод
def analytical_method(matrix):
    # Оптимальная стратегия игрока А
    p1 = (matrix[1][1] - matrix[1][0]) / (matrix[0][0] + matrix[1][1] - matrix[0][1] - matrix[1][0])
    if p1 < 0:
        p1 = 0
    elif p1 > 1:
        p1 = 1
    p2 = (matrix[0][0] - matrix[0][1]) / (matrix[0][0] + matrix[1][1] - matrix[0][1] - matrix[1][0])
    if p2 < 0:
        p2 = 0
    elif p2 > 1:
        p2 = 1
    v = matrix[0][0] * p1 + matrix[1][0] * p2

    print(pd.DataFrame(matrix, index=[f'A{i + 1}' for i in range(len(matrix))],
                       columns=[f'B{i + 1}' for i in range(len(matrix[0]))]))

    print(f'\n{round(p1*100, 2)}% всіх ходів має складати стратегія А1')
    print(f'{round(p2 * 100, 2)}% всіх ходів має складати стратегія А2')
    print(f'Така стратегія допоможе досягти найрелевантнішого виграшу у розмірі {round(v, 2)} очок')

    # Оптимальная стратегия игрока В
    q1 = (matrix[1][1] - matrix[0][1]) / (matrix[0][0] + matrix[1][1] - matrix[0][1] - matrix[1][0])
    if q1 < 0:
        q1 = 0
    elif q1 > 1:
        q1 = 1
    q2 = 1 - q1
    if q2 < 0:
        q2 = 0
    elif q2 > 1:
        q2 = 1
    v = matrix[0][0] * q1 + matrix[0][1] * q2

    print(f'\n{round(q1 * 100, 2)}% всіх ходів має складати стратегія B1')
    print(f'{round(q2 * 100, 2)}% всіх ходів має складати стратегія B2')
    print(f'Така стратегія допоможе досягти найменшого програшу')


# Графоаналитический метод
def graphical_method(matrix):
    figure, ax = plt.subplots(figsize=(4, 4))
    figure.suptitle('Графоаналітичний метод')
    ax.set_title('Гравець А')
    ax.set_xlabel('p')
    ax.set_ylabel('v')
    for i in range(len(matrix[0])):
        ax.plot([1, 0], [matrix[0][i], matrix[1][i]], '-o')

    data = pd.DataFrame(matrix, index=[f'A{i+1}' for i in range(len(matrix))],
                        columns=[f'B{i+1}' for i in range(len(matrix[0]))])
    print(data)

    print('\nПроаналізувавши графік, визначте стратегії гравця В, які будуть додані у спрощену матрицю.')

    plt.show()

    bn = [int(input('Введіть номер стратегії опонента: В'))-1 for i in range(2)]

    result = [[matrix[0][bn[0]], matrix[0][bn[1]]],
              [matrix[1][bn[0]], matrix[1][bn[1]]]]

    print('\nСпрощена до формату 2х2 платіжна матриця:\n')

    analytical_method(result)


# Выбираем метод поиска оптимальной стратегии на основе конфигурации матрицы
def method(matrix):
    # # matrix = [[random.randint(-20, 20) for i in range(2)] for i in range(2)]   # удалить
    # matrix = [[random.randint(-20, 20) for i in range(5)] for i in range(2)]   # удалить
    # # matrix = [[random.randint(-20, 20) for i in range(2)] for i in range(5)]   # удалить

    m = len(matrix)
    n = len(matrix[0])
    if (m == 2 and n > 2) or (m > 2 and n == 2):
        # matrix = [[random.randint(-20, 20) for i in range(2)] for i in range(2)]   # удалить
        graphical_method(matrix)
    elif m == 2 and n == 2:
        analytical_method(matrix)
    else:
        print('\nВикористовуй базовий метод / наближений метод')
        print('На жаль, метод для пошуку оптимальної стратегії для вказаної матриці ще відсутній :(\n')


# Создаём платёжную матрицу и проверяем её на наличие седловой точки
def table(m, n, a, b):
    matrix = [[random.randint(a, b) for i in range(m)] for j in range(n)]

    print('Згенерована платіжна матриця:\n')
    print(pd.DataFrame(matrix, index=[f'A{i + 1}' for i in range(len(matrix))],
                       columns=[f'B{i + 1}' for i in range(len(matrix[0]))]))

    # Нижняя цена игры
    minimum = max([min(row) for row in matrix])
    print()

    # Верхняя цена игры
    maximum = min([max([matrix[i][j] for i in range(5)]) for j in range(5)])

    print('Нижня ціна гри:', minimum)
    print('Максимальна ціна гри', maximum)

    # Поиск седловой точки
    if maximum == minimum:
        print('Сідлова точка:', maximum)
        print("Відхилення від стратегії з такою ціною обов'язково призведе до програшу.")

        print(pd.DataFrame(matrix, index=[f'A{i + 1}' for i in range(len(matrix))],
                           columns=[f'B{i + 1}' for i in range(len(matrix[0]))]))

    else:
        print('Платіжна матриця не містить сідлової точки.\n')

        # matrix = simplifying(matrix)
        matrix = two_x_n(matrix)

        # Выбор метода в зависимости от конфигурации матрицы
        method(matrix)

    return matrix


def main():
    table(5, 5, -20, 20)


if __name__ == '__main__':
    main()
