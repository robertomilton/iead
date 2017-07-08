from django.shortcuts import render
from .models import Person


def home(request):
    return render(request, 'core/index.html')


def person_list(request):
    persons = Person.objects.all()
    get_search = request.GET.get('search_box')
    if get_search is not None:
        persons = persons.filter(nome__icontains=get_search)
    ctx = {'persons': persons}
    return render(request, 'core/person_list.html', ctx)
