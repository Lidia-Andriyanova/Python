import model
import view
import logger

def button_click():
    value_a = view.get_value(1)
    value_b = view.get_value(2)
    operation = view.get_operation()
    if operation == '+':
        result = model.sum_num(value_a, value_b)
    elif operation == '-':
        result = model.sub_num(value_a, value_b)
    elif operation == '*':
        result = model.mult_num(value_a, value_b)
    elif operation == '/':
        result = model.div_num(value_a, value_b)
    #view.view_data(f'{value_a} {operation} {value_b}', result)
    op = f'{value_a} {operation} {value_b}'
    view.view_data(op, result)
    logger.operation_logger(op, result)