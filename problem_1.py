def stringify(quantity: int) -> str:
    """ Функция принимает на вход число и возвращает строку со склонением по падежам"""
    second_last = (quantity % 100) // 10  # Предпоследняя цифра числа
    last_one = quantity % 10  # Последняя цифра числа
    if last_one == 1 and second_last != 1:
        return f'{quantity} компьютер'
    elif last_one in range(2, 5) and second_last != 1:
        return f'{quantity} компьютера'
    else:
        return f'{quantity} компьютеров'


for i in range(1, 120):
    print(stringify(i))
