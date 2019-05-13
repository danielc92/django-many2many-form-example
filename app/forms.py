from models import Person, Hobby
from django import forms

class PersonForm(forms.Form):
    class Meta:
        model = Person
        fields = ['name', 'height', 'hobbies']


class HobbyForm(forms.Form):
    class Meta:
        model = Hobby
        fields = ['name']
