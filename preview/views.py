# from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    print 'home'
    return render_to_response("index.html")