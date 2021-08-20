from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'John doe',
        'title':'Blog post',
        'content':'new content',
        'date_posted':'August 28, 2018',
    },
    {
        'author':'Jane doe',
        'title':'Blog post 2',
        'content':'new content 2',
        'date_posted':'August 28, 2018',
    }
]


# Create your views here.
def index(request):
    context = {
        'posts':posts,
        'title':'Home page'
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title':'About page'
    }
    return render(request,'blog/about.html',context)