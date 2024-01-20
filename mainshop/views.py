from django.shortcuts import render, get_object_or_404
from django.http.response import Http404
from .models import Category, Product
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range

def main_page(request, category_id=None):
    categories = Category.objects.all()
    
    if category_id:
        products = Product.objects.filter(category__id=category_id).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')
 
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(current_page)
    
    paginator_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
    )

    return render(request, 'products/main.html', context={
        'categories': categories, 
        'products': page_obj,
        'pagination_range': paginator_range
    })

def details_products(request, product_id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details_product.html', {'product': product, 'categories': categories,})


def search(request):
    categories = Category.objects.all()
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    products = Product.objects.filter(
        Q(product_display_name__icontains=search_term) |
        Q(color__icontains=search_term),
    ).order_by('-id')

    return render(request, 'pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'products': products,
        'categories': categories,
    })


def create_account(request):
    return render(request, 'products/create_account.html')