from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request, # так будет всегда
        'gantt_chart/main.html', # Путь к шаблону
    )