from django.shortcuts import render, redirect
from .forms import HobbyForm, PersonForm

# Create your views here.
def create_hobby(request):

    if request.method == 'POST':
        form = HobbyForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)

            return redirect('success')
    else:

        form = HobbyForm()

    context = {'form': form, 'title':'Create a hobby!'}

    print(form.as_p)

    return render(request, 'create.html', context)


def create_person(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)

            return redirect('success')
    else:

        form = PersonForm()

    context = {'form': form, 'title':'Add a person!'}

    return render(request, 'create.html', context)



def success(request):

    return render(request, 'success.html', {})