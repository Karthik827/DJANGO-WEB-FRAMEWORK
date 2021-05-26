from django.shortcuts import render
from sessionApp.forms import NameForm,AgeForm,GfForm

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view(request):
    form = AgeForm()
    name = request.GET['name']
    request.session['name'] = name
    return render(request,'testapp/age.html',{'form':form})

def gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GfForm()
    return render(request,'testapp/gf.html',{'form':form})

def result_view(request):
    gf = request.GET['gf']
    request.session['gf']=gf
    return render(request,'testapp/result.html')