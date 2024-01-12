from django.shortcuts import render


def main_page(request):
    return render(request, 'products/main.html')

def details_product(request):
    return render(request, 'products/details_product.html')

def sign(request):
    return render(request, 'products/sign.html')