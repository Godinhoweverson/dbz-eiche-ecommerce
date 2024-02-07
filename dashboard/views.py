from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard_overview(request):
    return render(request, 'dashboard/dashboard_overview.html')

@login_required
def edit_myaccount(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        messages.success(request, f"Account Updated! Your changes have been saved.")
        user.save()

        return redirect('dashboard:dashboard_overview')

    return render(request, 'dashboard/edit_myaccount.html')