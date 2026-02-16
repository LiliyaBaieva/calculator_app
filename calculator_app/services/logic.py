import math

def calculate_logic(a, b, operation):
    try:
        # Конвертуємо вхідні дані
        num_a = float(a) if a and a.strip() != '' else 0.0
        num_b = float(b) if b and b.strip() != '' else 0.0

        res = None
        if operation == 'add':
            res = num_a + num_b
        elif operation == 'sub':
            res = num_a - num_b
        elif operation == 'mul':
            res = num_a * num_b
        elif operation == 'div':
            if num_b == 0: return "Помилка: / 0"
            res = num_a / num_b
        elif operation == 'extra':
            # Спеціальна функція за умовою a > 0
            if num_a < 0: return "Помилка: a < 0"
            res = math.sqrt(num_a)
        elif operation == 'plus_minus':
            res = num_a * -1
        
        # Застосовуємо форматування до 3 знаків перед поверненням
        return format_result(res) if res is not None else None
            
    except (ValueError, TypeError):
        return "Помилка вводу"

def format_result(value):
    if isinstance(value, (int, float)):
        # f"{value:.3f}" гарантує рівно три знаки після коми
        return "{:.3f}".format(value)
    return value