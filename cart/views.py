from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from django.contrib import messages
from django.conf import settings
from mainshop.models import Product

from django.contrib.auth.decorators import login_required


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = Cart(request)
    cart.add(product_id)
    messages.success(request, f"Added {product.product_display_name} to cart!")
    return render(request, 'cart/add-ons/menu_cart.html')


def cart(request):
    cart = Cart(request)
    items = []
    for item in cart:
        product = Product.objects.get(pk=item['product_id'])
        items.append({
            'product_id': item['product_id'],
            'product_display_name': product.product_display_name,
            'image': product.image,
            'price': product.price,
            'total_price': item['total_price'],
            'quantity': item['quantity'],
        })
    total_cost = cart.get_total_cost()
    return render(request,
                  'cart/cart.html',
                  {'items': items, 'total_cost': total_cost})


def success(request):
    return render(request, 'cart/success.html')


def update_cart(request, product_id, action):
    cart = Cart(request)
    if action == 'increment':
        cart.increment_quantity(product_id)
        messages.success(request, f" Incremented")
    elif action == 'decrement':
        cart.decrement_quantity(product_id)
        messages.success(request, f"removed 1 item from the cart!")

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product_id': product.id,  # Store the product ID
            'image': product.image,
            'price': product.price,
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }

    else:
        item = None

    response = render(request, 'cart/add-ons/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


def remove_from_cart(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove_item(product_id)
        messages.success(request,
                         f"Remove {product.product_display_name} to cart!")
        response_data = {'message': 'Item removed from the cart'}
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {'error': 'Internal Servel Error'}
        messages.success(
            request, f"Removed {product.product_display_name} from the cart!"
        )
        return JsonResponse(response_data, status=500)


@login_required
def checkout(request):
    pub_key = settings.STRIPE_PUBLIC_KEY
    return render(request, 'cart/checkout.html', {'pub_key': pub_key})


def hx_menu_cart(request):
    return render(request, 'cart/add-ons/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart/add-ons/cart_total.html')
