from django.shortcuts import render
from.import forms

# Create your views here.

def thankyou_view(request):
    return render(request,'testApp/thankyou.html')

def feedback_view(request):
    form = forms.FeedBackForm()
    if request.method=='POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("Form validation success and printing feeback info")
            print('Student Name: ',form.cleaned_data['name'])
            print('Student RollNO: ',form.cleaned_data['rollno'])
            print('Student Mail: ',form.cleaned_data['email'])
            print('Student FeedBack: ',form.cleaned_data['feedback'])
            return thankyou_view(request)

    return render(request,'testApp/feedback.html',{'form':form})