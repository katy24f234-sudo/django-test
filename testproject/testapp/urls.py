from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.all_tabs),
    path('',views.home,name='home')
]
