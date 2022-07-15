from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'checkListWS/home.html', {})

def about(request):
    return render(request, 'checkListWS/about.html', {})