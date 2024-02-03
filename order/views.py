from django.shortcuts import render

import json
import stripe

from django.conf import settings
from django.http import JsonResponse

from cart.cart import Cart
from .models import Order, OrderItem


def start_order(request):
    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0

    items = []
    YOUR_URL = 'https://8000-godinhoweve-dbzeicheeco-a7zpjf6y18f.ws-eu108.gitpod.io'

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])

        unit_amount_cents = int(product.price * 100)

        items.append({
            'price_data': {
                'currency': 'usd',
                'product_data':{
                    'name': product.product_display_name,
                },
                'unit_amount': unit_amount_cents,
            },
            'quantity': item['quantity']
        }
        )

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    session  = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = items,
        mode='payment',
        success_url = f'{YOUR_URL}/cart/success/',
        cancel_url =f'{YOUR_URL}/cart/'
      
    )

    payment_intent = session.payment_intent

    order = Order.objects.create(
        user = request.user,
        first_name = data['first_name'],
        last_name=data['last_name'], 
        email=data['email'], 
        phone=data['phone'], 
        address=data['address'], 
        zipcode=data['zipcode'], 
        place=data['place'],
        payment_intent=payment_intent,
        paid=True,
        paid_amount=total_price
    )

    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = OrderItem.objects.create(
            order=order, 
            product=product, 
            price=price, 
            quantity=quantity
        )

    cart.clear()

    return JsonResponse({'session': session, 'order':payment_intent})