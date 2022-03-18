from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Speech
from django.db.models import Q

def all_speeches(request):
    """ this shows every speech in the database """
    speeches = Speech.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('speeches'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            speeches = speeches.filter(queries)

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
