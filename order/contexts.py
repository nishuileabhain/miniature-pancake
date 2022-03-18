from decimal import Decimal
from django.conf import settings

def order_contents(request):
    """ list of ordered items"""
    order_items = []
    total = 0
    product_count = 0

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
        'product_count': product_count,
    }

    return context
