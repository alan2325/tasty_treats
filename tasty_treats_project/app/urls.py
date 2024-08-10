from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('element',views.element),
    path('menu',views.menu),
    path('blog-details',views.blogdetails),
    path('blog-home',views.blogdetails),
]