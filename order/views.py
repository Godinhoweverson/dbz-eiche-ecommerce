from django.shortcuts import render
from decimal import Decimal
import json
import stripe
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import JsonResponse

from cart.cart import Cart
from .models import Order, OrderItem
from mainshop.models import Product


def start_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        data = json.loads(request.body)
        total_price = 0

        items = []
        YOUR_URL = 'https://dbz-eiche-b8d414c8e346.herokuapp.com'

        for item in cart:

            product_id = item['product_id']
            quantity = item['quantity']
            product_instance = get_object_or_404(Product, pk=product_id)
            total_price += Decimal(product_instance.price) * quantity

            unit_amount_cents = int(Decimal(product_instance.price) * 100)

            items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data':{
                        'name': product_instance.product_display_name,
                    },
                    'unit_amount': unit_amount_cents,
                },
                'quantity': quantity
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
            product_id = item['product_id']
            quantity = item['quantity']
            product_instance = get_object_or_404(Product, pk=product_id)
            price = Decimal(product_instance.price) * quantity

            item = OrderItem.objects.create(
                order=order, 
                product=product_instance, 
                price=price, 
                quantity=quantity
            )

        cart.clear()

        return JsonResponse({'session': session, 'order':payment_intent})
    else:
        return JsonResponse({'error': 'GET request not supported for this endpoint'}, status=400)