from decimal import Decimal as dec

expression = ''

first_number = 0
second_number = 0
operation = ''
result = 0


def get_first_number():
    global first_number
    return first_number


def set_first_number(value):
    global first_number
    first_number = value


def get_second_number():
    global second_number
    return second_number


def set_second_number(value):
    global second_number
    second_number = value


def get_operation():
    global operation
    return operation


def set_operation(value):
    global operation
    operation = value


def get_result():
    global result
    return result


def addition():
    global first_number
    global second_number
    global result
    result = dec(str(float(first_number + second_number)))
    if result == int(result):
        result = int(result)


def difference():
    global first_number
    global second_number
    global result
    result = dec(str(float(first_number - second_number)))
    if result == int(result):
        result = int(result)


def multiplication():
    global first_number
    global second_number
    global result
    result = dec(str(float(first_number * second_number)))
    if result == int(result):
        result = int(result)


def division():
    global first_number
    global second_number
    global result
    result = dec(str(float(first_number / second_number)))
    if result == int(result):
        result = int(result)


def get_expression():
    global expression
    return expression


def set_expression(value):
    global expression
    expression = value
