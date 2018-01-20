from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    pais_nascimento = forms.CharField(initial='Brasil')

    class Meta:
        model = Person
        fields = '__all__'
