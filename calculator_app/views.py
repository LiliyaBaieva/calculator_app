from django.shortcuts import render
from .services.logic import calculate_logic, format_result

def calculator_view(request):
    result = None
    num1 = ""
    num2 = ""
    
    if request.method == "POST":
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        operation = request.POST.get('operation')
        
        raw_result = calculate_logic(num1, num2, operation)
        
        result = format_result(raw_result)
        
    return render(request, 'calculator_app/index.html', {
        'result': result,
        'num1': num1,
        'num2': num2
    })