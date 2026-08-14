from django.shortcuts import render , redirect
from .forms import PostCreateForm, CustomProfileform ,CustomUsercreationForm
from .models import Post,User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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
    if request.user.is_authenticated :
        return redirect('home')
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
    if request.method=='POST':
        profile_form=CustomProfileform(request.POST)
        user_form=CustomUsercreationForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user=user_form.save(commit=False)
            email=user_form.cleaned_data['email']
            user.email=email
            user.username=email
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            login(request , user)
            return redirect('home')
    else:    
        profile_form=CustomProfileform()
        user_form=CustomUsercreationForm()
    page='login'
    data={
    'page':page,   
    'profile_form':profile_form,
    'user_form':user_form
    }
    return render(request,'testapp/login_register.html',data)

def logoutpage(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    if request.method=='POST':
        profile_form=CustomProfileform(request.POST)
        user_form=CustomUsercreationForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user=user_form.save(commit=False)
            email=user_form.cleaned_data['email']
            user.email=email
            user.username=email
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            login(request , user)
            return redirect('home')
    else:
        profile_form=CustomProfileform()
        user_form=CustomUsercreationForm()
    data={
        'profile_form':profile_form,
        'user_form':user_form
    }
    return render(request,'testapp/login_register.html',data)