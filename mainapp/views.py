from django.shortcuts import render, redirect
from .forms import TeamForm

def index(request):
    print(request.user)

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TeamForm()

    return render(request, 'index.html', {'form': form})
