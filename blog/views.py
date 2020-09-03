from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author': 'Dmitriy',
        'title': 'Blog Post 1',
        'content': 'content for first post',
        'date_posted': 'august 30th 2020'
    },
    {
        'author': 'Dmitriy',
        'title': 'Blog Post 2',
        'content': 'content for first post',
        'date_posted': 'august 30th 2020'
    },
    {
        'author': 'Dmitriy',
        'title': 'Blog Post 3',
        'content': 'content for first post',
        'date_posted': 'august 30th 2020'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
