import math

def calculate_logic(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        return a / b if b != 0 else "Помилка: ділення на нуль"
    elif operation == 'extra':
        # корінь квадратний (a > 0)
        return math.sqrt(a)
    return None

def format_to_three_decimal_places(value):
    if isinstance(value, str):
        return value
    # Форматування без математичного округлення
    s = "{:.10f}".format(float(value))
    main_part, decimal_part = s.split('.')
    return f"{main_part}.{decimal_part[:3]}"