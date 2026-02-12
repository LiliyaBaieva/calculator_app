from django.shortcuts import render

from calculator_app.services.logic import calculate_logic, format_to_three_decimal_places

def calculator_view(request):
    result = None
    error = None
    
    if request.method == "POST":
        try:
            # Отримуємо дані та замінюємо кому на крапку для float
            num1 = float(request.POST.get('num1', 0).replace(',', '.'))
            num2 = float(request.POST.get('num2', 0).replace(',', '.'))
            op = request.POST.get('operation')

            # Перевірка умови ііііa > 0 для додаткової операції
            if op == 'extra' and num1 <= 0:
                error = "Для цієї операції Число A має бути більше 0!"
            else:
                raw_result = calculate_logic(num1, num2, op)
                result = format_to_three_decimal_places(raw_result)
                
        except ValueError:
            error = "Будь ласка, введіть коректні числа."
            
    return render(request, 'calculator_app/index.html', {'result': result, 'error': error})