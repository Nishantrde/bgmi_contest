# Inside views.py
from django.shortcuts import render, redirect
from .forms import TeamForm

def index(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace 'success_url' with the URL where you want to redirect after form submission
    else:
        form = TeamForm()
    
    return render(request, 'index.html', {'form': form})