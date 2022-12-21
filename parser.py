# Программа обрабатывает ввод строки:
# в виде Х.ХХХ (любое кол-во знаков после запятой)
# в виде целого числа
# в виде одной из операций ['+', '-', '*', '/'] - кроме ситуаций, описанных ниже
# где в качестве первого элемента указан элемент в виде -Х.XXX (любое кол-во знаков после запятой)

# Программа не обрабатывает следующие случаи:
# если в начале выражения (любой длины) есть один/несколько знаков ['+', '*', '/'] или несколько ['-']
# -> удаление ['+', '*', '/'] или повтора ['-']
# если в конце выражения (любой длины) есть один/несколько знаков ['+', '-', '*', '/'] -> удаление
# если в середине выражения (любой длины) есть повторение знаков ['+', '-', '*', '/'] -> удаление
# повторого знака
# наличие скобок и их учет в расчете выражения


from decimal import Decimal as dec


def first_parse(string: str) -> list:
    list = string.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/',
                                                                                                       ' / ').split()
    return list


def parse_cleaning(list: list) -> list:
    new_list = []
    for i in range(len(list)):
        split_point = list[i].split('.')
        if len(split_point) == 2 and split_point[0].isdigit() and split_point[1].isdigit():
            new_list.append(dec(str(float('.'.join(split_point)))))
        elif len(split_point) == 1 and split_point[0].isdigit():
            new_list.append(int(split_point[0]))
        elif len(split_point) == 1 and split_point[0] in ['+', '-', '*', '/']:
            new_list.append(split_point[0])
    return new_list


def empty_list_check(new_list: list) -> bool:
    var = 0
    if len(new_list) == 0:
        print('Введено неверное значение выражения, строка выражения пуста.')
        var = True
    return var


def first_negativ_element_check(new_list: list) -> list:
    if (new_list[0] == '-') and (isinstance(new_list[1], dec) or isinstance(new_list[1], int)):
        new_list[0] = dec(str(float((new_list[0] + str(new_list[1])))))
        new_list.pop(1)
    return new_list


def division_by_zero_check(new_list: list) -> bool:
    var = 0
    for i in range(len(new_list) - 1):
        if new_list[i] == '/' and new_list[i + 1] == 0:
            var = True
    return var


def result_of_expression(new_list: list) -> dec:
    while len(new_list) != 1:
        i = 0
        while ('*' in new_list or '/' in new_list) and i < len(new_list):
            if new_list[i] == '*':
                result = new_list[i - 1] * new_list[i + 1]
                new_list.pop(i)
                new_list.pop(i)
                new_list[i - 1] = dec(str(float(result)))
            elif new_list[i] == '/':
                result = new_list[i - 1] / new_list[i + 1]
                new_list.pop(i)
                new_list.pop(i)
                new_list[i - 1] = dec(str(float(result)))
            else:
                i += 1
        i = 0
        while ('+' in new_list or '-' in new_list) and i < len(new_list):
            if new_list[i] == '+':
                result = new_list[i - 1] + new_list[i + 1]
                new_list.pop(i)
                new_list.pop(i)
                new_list[i - 1] = dec(str(float(result)))
            elif new_list[i] == '-':
                result = new_list[i - 1] - new_list[i + 1]
                new_list.pop(i)
                new_list.pop(i)
                new_list[i - 1] = dec(str(float(result)))
            else:
                i += 1

    if new_list[0] == int(new_list[0]):
        new_list[0] = int(new_list[0])

    total = f'Результат введенного выражения - это: {new_list[0]}'
    return total
