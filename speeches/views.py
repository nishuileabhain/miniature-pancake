from django.shortcuts import render
from .models import Speech

def all_speeches(request):
    """ this shows every speech in the database """
    speeches = Speech.objects.all()
    context = {
        'speeches' : speeches,
    }

    return render(request, 'speeches/speeches.html', context)

# def home(request):
#     return render(request, 'speeches/home.html')

# def order(request):
#     return order(request, 'speeches/order.html')
