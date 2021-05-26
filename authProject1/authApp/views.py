from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authApp.forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_page_view(request):
    return render(request,'testapp/javaexam.html')
@login_required
def python_page_view(request):
    return render(request,'testapp/python.html')
@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitude.html')


def logout_view_page(request):
    return render(request,'testapp/logout.html')


def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

    