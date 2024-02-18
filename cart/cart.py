from django.conf import settings
from mainshop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for product_id, item in self.cart.items():
            product_id = int(product_id)
            try:
                product = Product.objects.get(pk=product_id)
                item['product_id'] = product_id
                item['total_price'] = int(product.price * item['quantity'])
                yield item
            except Product.DoesNotExist:
                pass

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        self.save()

    def increment_quantity(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += 1
            self.save()

    def decrement_quantity(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= 1

            if self.cart[product_id]['quantity'] <= 0:
                self.remove_item(product_id)
            else:
                self.save()

    def remove_item(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        total_cost = 0
        for product_id, item in self.cart.items():
            try:
                product = Product.objects.get(pk=int(product_id))
                total_cost += int(product.price) * item['quantity']
            except Product.DoesNotExist:
                pass
        return total_cost

    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None
