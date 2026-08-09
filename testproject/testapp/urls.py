from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.all_tabs),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('creatpost/',views.Post_create_form,name='creatpost')
]
