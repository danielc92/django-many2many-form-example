from .models import Person, Hobby
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'height', 'hobbies']


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name']
