from django.shortcuts import render

# Create your views here.

def view_order(request):
    """ A view that renders the bag contents page """

    return render(request, 'order/order.html')
