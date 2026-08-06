from django.shortcuts import render

def all_tabs(request):
    return render(request,'testapp/all_tabs.html')
