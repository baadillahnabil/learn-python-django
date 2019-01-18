from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'message': 'This is a message from views.py inside method index. Template changed'
    }
    return render(request, 'BasicApp/index.html', data)
