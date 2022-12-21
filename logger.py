def log_simple_calculation_start():
    with open('logger_calculation_simple.txt', 'w', encoding='UTF-8') as file:
        file.write('Используется кнопочный калькулятор\n')


def log_simple_calculation_result(result: str):
    with open('logger_calculation_simple.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{result}\n')


def log_string_calculation_start():
    with open('logger_calculation_string.txt', 'w', encoding='UTF-8') as file:
        file.write('Используется строчный калькулятор\n')


def log_string_calculation_expression(expression: str):
    with open('logger_calculation_string.txt', 'a', encoding='UTF-8') as file:
        file.write(f'Введенное выражение - это: {expression}\n')


def log_string_calculation_result(result: str):
    with open('logger_calculation_string.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{result}\n')
