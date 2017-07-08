from django.shortcuts import render
from .models import Person


def home(request):
    return render(request, 'core/index.html')


def person_list(request):
    persons = Person.objects.all()
    ctx = {'persons': persons}
    return render(request, 'core/person_list.html', ctx)
