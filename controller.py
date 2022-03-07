import re
from unittest import result
import model_calc as mod
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
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
