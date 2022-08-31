from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    username = request.POST.get('user_name','default')
    password = request.POST.get('password','default')
    confirm_password = request.POST.get('confirm_password','default')
    if password == confirm_password and len(username) != 0:
        return render(request, 'index.html')
    else:
        return HttpResponse("<h1>Error</h1>")


def check_credentials(request):
    username = request.GET.get('user_name','default')
    password = request.GET.get('password','default')
    params = {
        "User_Name" : username,
        "Password" : password
    }
    return render(request,'home.html',params)



def signup(request):
    return render(request,'signup.html')



