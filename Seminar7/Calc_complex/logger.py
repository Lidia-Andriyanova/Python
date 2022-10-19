from datetime import datetime as dt
from time import time

def operation_logger(op, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time}: {op} = {result}\n')

