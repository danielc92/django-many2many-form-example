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

        form = HobbyForm(request.GET)

    context = {'form': form, 'title':'create a hobby!'}

    return render(request, 'create', context)

def success(request):

    return render(request, 'success.html', {})