from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.all_tabs,name='posts'),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('creatpost/',views.Post_create_form,name='creatpost'),
    path('post_details/<str:id>',views.post_details,name='post_details'),
    path('post_edit/<str:id>',views.post_edit,name='post_edit'),
    path('post_delete/<str:id>',views.post_delete,name='post_delete')
]
