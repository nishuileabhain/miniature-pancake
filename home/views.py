from django.shortcuts import render


def index(request):
    """ this view returns the index page """
    return render(request, 'home/index.html')
