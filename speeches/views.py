from django.shortcuts import render, get_object_or_404
from .models import Speech

def all_speeches(request):
    """ this shows every speech in the database """
    speeches = Speech.objects.all()
    context = {
        'speeches': speeches,
    }

    return render(request, 'speeches/speeches.html', context)


def speech_detail(request, speech_id):
    """ this shows the details of a particular speech """
    speech = get_object_or_404(Speech, pk=speech_id)
    context = {
        'speech': speech,
    }

    return render(request, 'speeches/speech_detail.html', context)


# def home(request):
#     return render(request, 'speeches/home.html')

# def order(request):
#     return order(request, 'speeches/order.html')
