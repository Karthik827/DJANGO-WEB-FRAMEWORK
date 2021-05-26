from django.shortcuts import render
from registerApp import forms

# Create your views here.

def student_view(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        form.save(commit=True)
        print('formdata inserted to database successfully')

    return render(request,'testapp/register.html',{'form':form})