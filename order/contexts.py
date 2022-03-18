from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from speeches.models import Speech

def order_contents(request):
    """ list of ordered items"""
    order_items = []
    total = 0
    speech_count = 0
    order = request.session.get('order', {})

    for item_id, quantity in order.items():
        speech = get_object_or_404(Speech, pk=item_id)
        total += quantity * speech.price
        speech_count += quantity
        order_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'speech': speech,
        })

    # if total < settings.FREE_DELIVERY_THRESHOLD:
    #     delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    #     free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    # else:
    #     delivery = 0
    #     free_delivery_delta = 0
    
    # grand_total = delivery + total
    
    context = {
        'order_items': order_items,
        'total': total,
        'speech_count': speech_count,
    }

    return context
