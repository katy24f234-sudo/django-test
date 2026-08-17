from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.all_tabs,name='posts'),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('creatpost/',views.Post_create_form,name='creatpost'),
    path('post_details/<str:id>',views.post_details,name='post_details'),
    path('post_edit/<str:id>',views.post_edit,name='post_edit'),
    path('post_delete/<str:id>',views.post_delete,name='post_delete'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('logout/',views.logoutpage,name='logoutpage'),
    path('product_details/<str:id>',views.product_details,name='product_details'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('delete_cart_item/<str:id>',views.delete_cart_item,name='delete_cart_item'),
    path('update_cart',views.update_cart,name='update_cart')
]
