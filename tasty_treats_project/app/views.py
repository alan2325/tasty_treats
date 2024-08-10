from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact-us.html')
def element(req):
    return render(req,'element.html')
def menu(req):
    return render(req,'menu.html')