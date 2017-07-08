from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email', 'funcao')
    list_display = ('nome', 'email', 'fone', 'celular')
