from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")

def adminLogin(request):
    return render(request, "adminLogin.html")

def base(request):
    return render(request, "base.html")

def forgotPage(request):
    return render(request, "forgotPage.html")

def forgotPageSuccessful(request):
    return render(request, "forgotPageSuccessful.html")
