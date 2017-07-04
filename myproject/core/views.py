from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def persons(request):
    return render(request, 'core/persons.html')
