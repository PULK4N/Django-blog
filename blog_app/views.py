from django.shortcuts import render

posts = [
    {
        'author' : 'Pupi',
        'title' : 'Blog post 1',
        'content' : 'First page content',
        'date_posted' : 'Mart 27, 2022',
    },
    {
        'author' : 'Pupi2',
        'title' : 'Blog post 2',
        'content' : 'Sec page content',
        'date_posted' : 'Mart 28, 2022',
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog_app/home.html', context)

def about(request):
    return render(request,'blog_app/about.html', { 'title' : 'About this page'})