from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('hello world')


def tasklist(request):
    return render(request, 'task/list.html')

def yourname(request, name):
    return render(request, 'task/yourname.html', {'name': name})