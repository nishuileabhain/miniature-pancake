from django.shortcuts import render

def home(request):
    return render(request, 'speeches/home.html')

def order(request):
    return order(request, 'speeches/order.html')
