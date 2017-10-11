from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'core/index.html')


@login_required
def person_list(request):
    ''' Uma view de todas as pessoas. '''
    persons = Person.objects.all()
    get_search = request.GET.get('search_box')
    if get_search is not None:
        persons = persons.filter(nome__icontains=get_search)
    ctx = {'persons': persons}
    return render(request, 'core/person_list.html', ctx)


@login_required
def person_detail(request, pk):
    ''' Uma view dos detalhes de cada pessoa '''
    person = Person.objects.get(pk=pk)
    ctx = {'person': person}
    return render(request, 'core/person_detail.html', ctx)


@login_required
def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/person/%d/' % obj.pk)
    else:
        form = PersonForm()
    ctx = {'form': form}
    return render(request, 'core/person_form.html', ctx)


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
