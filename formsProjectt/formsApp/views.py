from django.shortcuts import render
from.import forms

# Create your views here.
def studentregisterview(request):
    form = forms.StudentRegister()
    return render(request,'testApp/register.html',{'form':form})