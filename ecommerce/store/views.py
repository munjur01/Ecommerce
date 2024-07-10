from django.shortcuts import render, redirect

def IndexView(request):

    return render(request, 'index.html')