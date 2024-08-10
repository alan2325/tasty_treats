from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact-us.html')
def element(req):
    return render(req,'elements.html')
def menu(req):
    return render(req,'menu.html')
def blogdetails(req):
    return render(req,'blog-details.html')
def bloghome(req):
    return render(req,'blog-home.htm')