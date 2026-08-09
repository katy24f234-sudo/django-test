from django.shortcuts import render
from .forms import PostCreateForm

def all_tabs(request):
    return render(request,'testapp/all_tabs.html')

def home(request):
    return render(request,'testapp/home.html')

def cart(request):
    return render(request,'testapp/cart.html')

def Post_create_form(request):
    form = PostCreateForm()
    data = {
        'form' : form
    }
    return render(request,'testapp/creatpost.html',data)
