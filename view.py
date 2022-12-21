from decimal import Decimal as dec

def first_input():
    first_input = input('Введите число или строчное выражение: ')
    return first_input


def input_number() -> dec:
    while True:
        try:
            number = float(input('Введите число:  '))
            number = dec(str(number))
            if number == int(number):
                number = int(number)
            return number
        except:
            print('Введено неверное значение')


def input_operation() -> str:
    oper = input('Введите операцию: ')
    if oper in ['+', '-', '/', '*', '=']:
        return oper
    else:
        print('Введено неверное значение операции')
        return input_operation()

#Иначе:
# def input_operation() -> str:
#     while True:
#         oper = input('Введите операцию: ')
#         if oper in ['+', '-', '/', '*', '=']:
#             return oper
#         else:
#             print('Введено неверное значение операции')

def print_data(value):
    print(value)

def print_division_by_zero():
    print('На ноль делить нельзя!')

def log_off_simple_calculation():
    print('Расчет окончен.')

def log_off_end():
    print('Спасибо, до свидания!')






