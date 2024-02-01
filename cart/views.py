from django.shortcuts import render
from .cart import Cart
from django.conf import settings
from mainshop.models import Product
from django.contrib.auth.decorators import login_required


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/add-ons/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')

def success(request):
    return render(request, 'cart/success.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity =quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.product_display_name,
                'image': product.image,
                'price': product.price
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/add-ons/cart_item.html', {'item':item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def hx_menu_cart(request):
    return render(request, 'cart/add-ons/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/add-ons/cart_total.html')