def print_multiplication_table(number: int) -> None:
    """ Функция выводит таблицу умножения для заданного числа """
    print('', *range(1, number + 1), sep='\t')  # Вывод первой строки
    for row in range(1, number + 1):
        for col in range(number + 1):
            if col == 0:  # Вывод первого столбца
                print(row, end='\t')
                continue
            print(row * col, end='\t')  # Вывод результата перемножения
        else:
            print('')


print_multiplication_table(9)
