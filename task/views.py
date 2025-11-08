from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'admin_today' : 'Вася'}
    return render(
        request,
        'task/main.html',
        context
    )