from django.shortcuts import render
from .forms import HobbyForm, PersonForm

# Create your views here.
def create_person(request):

    if request.method == 'POST':
        form = request.POST