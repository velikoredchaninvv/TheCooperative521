from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'admin_today' : 'Вася' # Позже эти данные можно взять из базы данных
    }
    return render( # Функция 'рендерит' шаблон, наполняет данными шаблон html страницы
        request,                         # так всегда. ЭТО ПЕРВЫЙ ПАРАМЕТР ФУНКЦИИ Render
        'mainpage/index.html',            # Путь к шаблону после templates. ЭТО ВТОРОЙ ПАРАМЕТР ФУНКЦИИ Render
        context # а находит он его потому что выше строкой указан путь до конкретного файла html. ЭТО ТРЕТИЙ ПАРАМЕТР ФУНКЦИИ Render
    )