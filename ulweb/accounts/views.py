from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.hashers import check_password
from .forms import UserForm, EditUserForm
from .models import UserInfo
from django.utils.decorators import decorator_from_middleware



def signup(request):
    if 'user_id' in request.session:
        return redirect('home')
    if request.POST:
        frm = UserForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')
    else:
        frm = UserForm()
        
    return render(request, 'signup.html', {'frm': frm})


def login_user(request):
    if 'user_id' in request.session:
        return redirect('home')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserInfo.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.pk
                return redirect('home')
            else:
                error_message = 'Invalid Username or Password'
        except UserInfo.DoesNotExist:
                error_message = 'Invalid Username or Password'
        return render(request, 'login.html',  {'error': error_message})
    return render(request, 'login.html') 


admin_username = 'admin'
admin_password = 'admin123'

def admin_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == admin_username and password == admin_password:
            return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})

    return render(request, 'admin_login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user_dashboard(request):
    query = request.GET.get('q')
    if query:
        user_details = UserInfo.objects.filter(
            firstname__icontains=query) | UserInfo.objects.filter(
            lastname__icontains=query) | UserInfo.objects.filter(
            email__icontains=query) | UserInfo.objects.filter(
            username__icontains=query)
    else:
        user_details = UserInfo.objects.all()
        
    return render(request, 'user_dashboard.html', {'users': user_details})

def purchase_details(request):
    return render(request, 'purchase_details.html')

def manage_user(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.POST:
        if 'save' in request.POST:
            frm = EditUserForm(request.POST, instance=user)
            if frm.is_valid():
                frm.save()
                return redirect('admin_home')
        elif 'delete' in request.POST:
            user.delete()
            return redirect('admin_home')
    else:
        frm = EditUserForm(instance=user)
    
    return render(request, 'manage_user.html', {'frm': frm, 'user': user})




