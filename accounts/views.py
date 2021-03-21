from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    user_form = request.POST.get('user')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=user_form, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha incorretos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'Sessão encerrada, realize login novamente')
    return redirect('index')


def signup(request):
    if request.method != 'POST':
        return render(request, 'accounts/signup.html')
    
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirmPassword')

    if not firstName or not lastName or not email \
        or not user or not password or not confirmPassword:
        messages.error(request, 'Preencha todos os campos para continuar')
        return render(request, 'accounts/signup.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Insira um endereço de e-mail válido')
        return render(request, 'accounts/signup.html')
    
    if len(password) < 8 or len(confirmPassword) < 8:
        messages.error(request, 'A senha deve ter no mínimo 8 caracteres')
        return render(request, 'accounts/signup.html')
    
    if password != confirmPassword:
        messages.error(request, 'As senhas informadas não coincidem')
        return render(request, 'accounts/signup.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'Este nome de usuário já existe')
        return render(request, 'accounts/signup.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Endereço de e-mail já cadastrado')
        return render(request, 'accounts/signup.html')

    messages.success(request, 'Cadastro realizado!')
    user = User.objects.create_user(
        username=user,
        email=email,
        password=password,
        first_name=firstName,
        last_name=lastName,
    )
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
