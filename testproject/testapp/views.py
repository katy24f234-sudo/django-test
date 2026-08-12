from django.shortcuts import render , redirect
from .forms import PostCreateForm
from .models import Post,User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='loginpage')
def Post_create_form(request):
    if(request.method == 'POST'):
        form = PostCreateForm(request.POST,request.FILES)
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

@login_required(login_url='loginpage')
def post_edit(request,id):
    post=Post.objects.get(pk=id)
    if request.method=='POST':
        form=PostCreateForm(request.POST,instance=post)
        if form.is_valid():
            # post.title=form.data.get('title')
            # post.content=form.data.get('content')
            post.save()
            return redirect('posts')
    data = {
        'post':post
    }
    return render(request,'testapp/post_edit.html',data)

@login_required(login_url='loginpage')
def post_delete(request, id):
    post=Post.objects.get(pk=id)
    if request.method=='POST':
        post.delete()
        return redirect('posts')
    data = {
            'post':post
        }
    return render(request,'testapp/post_delete.html',data)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.add_message(request,messages.ERROR,"username not found")
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request , user)
            return redirect('home')
        messages.add_message(request,messages.ERROR,"wrong username or password")
    return render(request,'testapp/login_register.html')

def logoutpage(request):
    logout(request)
    return redirect('home')