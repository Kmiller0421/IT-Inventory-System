from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")

def struct(request):
    return render(request, "struct.html")

def base(request):
    return render(request, "base.html")
