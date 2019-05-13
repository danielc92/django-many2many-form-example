from django.shortcuts import render, redirect
from .forms import HobbyForm, PersonForm
from .models import Hobby, Person

# Create your views here.
def create_hobby(request):

    if request.method == 'POST':
        form = HobbyForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            Hobby.objects.create(**cd)

            return redirect('success')
    else:

        form = HobbyForm()

    context = {'form': form, 'title':'Create a hobby!'}

    return render(request, 'create.html', context)


def create_person(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            h_data = cd['hobbies']
            p_data = {k:v for k, v in cd.items() if k != 'hobbies'}

            person = Person.objects.create(**p_data)
            
 
            for hobby in h_data:
                person.hobbies.add(hobby)

            return redirect('success')
    else:

        form = PersonForm()

    context = {'form': form, 'title':'Add a person!'}

    return render(request, 'create.html', context)



def success(request):

    return render(request, 'success.html', {})