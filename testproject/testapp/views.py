from django.shortcuts import render , redirect
from .forms import PostCreateForm
from .models import Post
from django.db.models import Q

def all_tabs(request):
    q=request.GET.get('q')
    Posts =Post.objects.all()
    if q:
        posts_filtered=Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    else :
        posts_filtered=Posts  
    data = {
        'Posts':Posts,
        'post_f':posts_filtered,
        'q':q
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
def post_edit(request,id):
    post=Post.objects.get(pk=id)
    if request.method=='POST':
        form=PostCreateForm(request.POST)
        if form.is_valid():
            post.title=form.data.get('title')
            post.content=form.data.get('content')
            post.save()
            return redirect('posts')
    data = {
        'post':post
    }
    return render(request,'testapp/post_edit.html',data)