from django.shortcuts import render , redirect
from .forms import PostCreateForm
from .models import Post

def all_tabs(request):
    Posts =Post.objects.all()
    data = {
        'Posts':Posts
    }
    return render(request,'testapp/all_tabs.html',data)

def home(request):
    return render(request,'testapp/home.html')

def cart(request):
    return render(request,'testapp/cart.html')

def Post_create_form(request):
    if(request.method == 'POST'):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = PostCreateForm()
    data = {
        'form' : form
    }
    return render(request,'testapp/creatpost.html',data)

def post_details(request,id):
    post=Post.objects.get(pk=id)
    data= {
        'post':post
    }
    return render(request,'testapp/post_details.html',data)