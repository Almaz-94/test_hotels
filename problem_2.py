
import math


def get_common_divisors(numbers: list[int]) -> list[int]:
    """ Функция возвращает все общие делители чисел в заданном списке"""
    divisors = []
    greatest_cd = numbers[0]
    for elem in numbers[1::]:  # Поочередно вычисляем НОД всех чисел
        greatest_cd = math.gcd(greatest_cd, elem)
    # greatest_cd - итоговый НОД списка numbers

    for divisor in range(1, greatest_cd//2+1):  # Ищем все делители числа greatest_cd (итогового НОД)
        if greatest_cd % divisor == 0:
            divisors.append(divisor)  # Делители НОД и будут являться всеми общими делителями списка

    divisors.append(greatest_cd)
    return divisors


arr = [120, 360, 240]
print(get_common_divisors(arr))
