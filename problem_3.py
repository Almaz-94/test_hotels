import math


def get_prime_numbers(left: int, right: int) -> list[int]:
    """ Функция возвращает список простых чисел в заданном диапазоне """
    prime_numbers = []

    if left > right:  # Проверка корректности диапазона
        raise ValueError('Неправильно заданный диапазон')
    elif right < 2:
        return []

    left = math.ceil(left)  # Проверка введения целых чисел
    right = int(right)

    left = 2 if left < 2 else left  # Убираем отрицательные числа

    for number in range(left, right+1):
        for denominator in range(2, int(number/2)+1):  # Для каждого числа ищем делители
            if number % denominator == 0:
                break  # Если находим делитель - выходим из цикла (число не простое)
        else:
            prime_numbers.append(number)  # Если цикл завершился без break, то это число простое
    return prime_numbers


print(get_prime_numbers(2, 100))
