from django.contrib.auth import logout as lgout, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AccountAuthenticationForm, AccountUpdateForm, AddPatient
from .models import PatientInformation


# Create your views here.
def logout(request):
    lgout(request)
    return redirect("login")


def index(request):
    if request.user.is_authenticated:
        if request.user.group == 'Approver':
            patient = PatientInformation.objects.filter(is_approved=False)
        else:
            patient = PatientInformation.objects.all()
    account = {
        "id": request.user.id,
        "name": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "profile_picture_path": request.user.profile_picture_path,
        'group': request.user.group,
        'is_superuser': request.user.is_superuser
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
                    'profile_picture_path': request.user.profile_picture_path,
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
        'group': request.user.group,
    } if request.user.is_authenticated else None
    context = {
        "account": account,
    }

    form = AddPatient(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = AddPatient()
        return redirect('home')

    context['form'] = form

    if request.user.is_authenticated:
        if request.user.group == 'Data Entry':
            return render(request, 'addPatient.html', context)
        else:
            return redirect('home')
    else:
        return redirect('login')


def patient_page(request, slug):
    account = {
        "id": request.user.id,
        "name": request.user.username,
        "email": request.user.email,
        "is_superuser": request.user.is_superuser,
        "group": request.user.group,
    } if request.user.is_authenticated else None
    context = {
        "account": account,
    }
    patient = get_object_or_404(PatientInformation, slug=slug)
    context['patient'] = patient
    if request.user.is_authenticated:
        return render(request, 'patient_page.html', context)
    else:
        return redirect('login')
