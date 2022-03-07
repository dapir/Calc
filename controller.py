import re
from unittest import result
import model_calc as mod
import view

def button_click():
    chos = int(input('Complex - (0) or not - (1) - '))
    if chos == 0:
        value_a = view.get_int()
        value_b = view.get_int()
    elif chos == 1:
        value_a = view.get_complex()
        value_b = view.get_complex()
    
    mod.fun(value_a, value_b)
    que = input('Выберите действие (+,-,*,/): ')
    if que == '+':
        result = mod.sum()
    elif que == '-':
        result = mod.diff()
    elif que == '*':
        result = mod.mult()
    elif que == '/':
        result = mod.div()

    view.view_data(result)
