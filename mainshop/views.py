from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import Http404
from mainshop.models import Category, Product, Comment
from cart.cart import Cart
from .forms import CommentForm, EditCommentForm
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range


def main_page(request, category_id=None):
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(
            category__id=category_id).order_by('-id')
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
    comments = product.comment_set.all().order_by('created_at')

    cart = Cart(request)
    in_cart = cart.get_item(product_id) is not None

    paginator = Paginator(comments, 2)
    page = request.GET.get('page')
    comments = paginator.get_page(page)

    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.user = request.user
                comment.save()
                return redirect('details_products', product_id=product.id)
            else:
                print("Form has errors:", form.errors)
        else:
            return redirect('account_login')

    return render(request,
                  'products/details_product.html',
                  {'product': product,
                   'categories ': categories,
                   'form': form,
                   'comments': comments,
                   'in_cart': in_cart})


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = EditCommentForm(instance=comment)

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details_products', product_id=comment.product.id)

    return render(request,
                  'global/partials/edit_comment.html',
                  {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('details_products', product_id=comment.product.id)
    return render(request,
                  'global/partials/delete_comment.html', {'comment': comment})


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


def handler404(request, exception):
    return render(request, 'status-code/not_found404.html', status=404)


def handler500(request, exception):
    return render(request, 'status-code/server_error500.html', status=500)


def handler403(request, exception):
    return render(request, 'status-code/forbidden403.html', status=403)


def privacy_policy(request):
    return render(request, 'global/partials/privacy_policy.html')
