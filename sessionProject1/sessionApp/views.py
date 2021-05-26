from django.shortcuts import render

# Create your views here.

def page_view_count(request):
    count = request.session.get('count',0)
    newcount = count+1
    request.session['count'] = newcount
    return render(request,'testapp/count.html',{'count':newcount})