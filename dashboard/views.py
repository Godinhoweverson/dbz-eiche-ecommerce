from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
@login_required
def myaccount(request):
    return render(request, 'dashboard/myaccount')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user.request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')

    return render(request, 'dashboard/edit_myaccount.html')