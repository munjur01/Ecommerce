from django.shortcuts import render, redirect
from .forms import ContactForm

def IndexView(request):

    return render(request, 'index.html')

def ContactView(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})
