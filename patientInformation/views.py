from django.shortcuts import render, redirect
from django.contrib.auth import logout as lgout, authenticate, login

from .forms import AccountAuthenticationForm, AccountUpdateForm
from .models import PatientInformation, Account


# Create your views here.
def logout(request):
    lgout(request)
    return redirect("login")


def index(request):
    patient = PatientInformation.objects.all()
    account = {
        "id": request.user.id,
        "name": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "profile_picture_path": request.user.profile_picture_path,
        'group': request.user.group
    } if request.user.is_authenticated else None

    if not request.user.is_authenticated:
        return redirect('login')

    context = {
        'object': patient,
        'account': account
    }

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            form = AccountUpdateForm(
                initial={
                    'email': request.user.email,
                    'username': request.user.username,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                }
            )
        context['account_form'] = form
    return render(request, 'homePage.html', context)


def loginPage(request):
    return render(request, 'login.html', {})


def loginadmin(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'loginAdmin.html', context)


def addpatient(request):
    account = {
        "id": request.user.id,
        "name": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "profile_picture_path": request.user.profile_picture_path,
        'group': request.user.group
    } if request.user.is_authenticated else None
    context = {
        "account": account,
    }
    if request.user.is_authenticated:
        if request.user.group == 'Data Entry':
            return render(request, 'addPatient.html', context)
        else:
            return redirect('home')
    else:
        return redirect('login')
