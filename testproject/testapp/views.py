from django.shortcuts import render , redirect,get_object_or_404
from .forms import PostCreateForm, CustomProfileform ,CustomUsercreationForm , CustomUserEditForm ,OrderReceipt
from .models import Post,User,Product,Cart,Cartitem,CustomProfile,Order,Orderitem
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
    products=Product.objects.all()
    return render(request,'testapp/home.html',{'products':products})

@login_required(login_url='loginpage')
def cart(request):
    cart=Cart.objects.get(user=request.user)
    cartitems=cart.items.all()
    return render(request,'testapp/cart.html',{'cartitems':cartitems,'cart':cart})

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

def product_details(request,id):
    product=Product.objects.get(pk=id)
    data= {
        'product':product
    }
    return render(request,'testapp/product_details.html',data)

@login_required(login_url='loginpage')
def add_to_cart(request):
    product_id=request.POST.get("product_id")
    page=request.POST.get("page")
    product=get_object_or_404(Product,id=product_id)
    cart,_=Cart.objects.get_or_create(user=request.user)
    cartitem,created=Cartitem.objects.get_or_create(cart=cart,product=product)
    if not created:
        cartitem.quantity+=1
        cartitem.save()
    return redirect(page)

def delete_cart_item(request,id):
    cartitem=get_object_or_404(Cartitem,pk=id,cart__user=request.user)
    cartitem.delete()
    return redirect('cart')

def update_cart(request):
    cart,_=Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        for item in cart.items.all():
            quantity=request.POST.get(f'number{item.id}')
            if int(quantity) >= 1:
                item.quantity=int(quantity)    
                item.save()
        return redirect('cart')
    
@login_required(login_url='loginpage')
def checkout(request):
    profile=get_object_or_404(CustomProfile,user=request.user)
    cart=get_object_or_404(Cart,user=request.user)
    cartitems=cart.items.all()
    return render(request,'testapp/checkout.html',{'profile':profile,'cart':cart,'cartitems':cartitems})

@login_required(login_url='loginpage')
def edit_profile(request):
    user=request.user
    profile=user.profile
    if request.method == "POST":
        profile_form=CustomProfileform(request.POST , instance=profile)
        user_form=CustomUserEditForm(request.POST , instance=user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('checkout')
    profile_form=CustomProfileform(instance=profile)
    user_form=CustomUserEditForm(instance=user)
    return render(request,'testapp/edit_profile.html',{'profile_form':profile_form,'user_form':user_form})

@login_required(login_url='loginpage')
def cart_to_order(request):
    cart=get_object_or_404(Cart,user=request.user)
    if cart.item_count !=0:
        cartitems=cart.items.all()
        order=Order.objects.create(user=request.user,total=cart.total)
        for item in cartitems:
            orderitem=Orderitem.objects.create(order=order,name=item.product.name,price=item.product.price,quantity=item.quantity,total=item.total)
        cart.delete()
        form=OrderReceipt(instance=order)
        orderitems=order.items.all()
        return render(request,'testapp/order_preview.html',{'order':order,'form':form,'orderitems':orderitems})
    else:
        return redirect('home')

def orders_list(request):
    orders=Order.objects.filter(user=request.user)
    return render(request,'testapp/orders.html',{'orders':orders})

def add_receipt_image(request,id):
    order=get_object_or_404(Order,pk=id,user=request.user)
    if(request.method == 'POST'):
        form = OrderReceipt(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')