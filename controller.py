import view
import model
import parser
import logger
import os


def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)


def input_second_number():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second_number(number)
            break


def solution_simple_calculation():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()

    result_str = f'{model.get_first_number()} {model.get_operation()} {model.get_second_number()} = {model.get_result()}'
    logger.log_simple_calculation_result(result_str)
    view.print_data(result_str)
    model.set_first_number(model.get_result())


def start():
    while True:
        input_data = view.first_input()
        model.set_expression(input_data)
        list = parser.first_parse(model.get_expression())
        list = parser.parse_cleaning(list)
        if parser.empty_list_check(list):
            break
        list = parser.first_negativ_element_check(list)
        if len(list) == 1:
            if os.path.exists('logger_calculation_simple.txt'):
                pass
            else:
                logger.log_simple_calculation_start()
            number = list[0]
            model.set_first_number(number)
            while True:
                input_operation()
                if model.get_operation() == '=':
                    view.log_off_simple_calculation()
                    break
                input_second_number()
                solution_simple_calculation()
        else:
            if os.path.exists('logger_calculation_string.txt'):
                logger.log_string_calculation_expression(model.get_expression())
            else:
                logger.log_string_calculation_start()
                logger.log_string_calculation_expression(model.get_expression())
            if parser.division_by_zero_check(list):
                view.print_division_by_zero()
            else:
                result = parser.result_of_expression(list)
                view.print_data(result)
                logger.log_string_calculation_result(result)
        retry = input('Посчитать еще одно выражение? (y/n):  ')
        if retry == 'n':
            view.log_off_end()
            break
