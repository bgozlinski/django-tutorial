from django.shortcuts import render

POSTS = [
    {
        "author": "Devs-Mentoring.pl",
        "title": "First post",
        "content": "First post content",
        "date": "28 April 2021"
    },
    {
        "author": "Devs-Mentoring.pl",
        "title": "Second post",
        "content": "Second post content",
        "date": "29 April 2021"
    }
]

def home(request):
    return render(request, "blog/home.html", {"title": "Home", "posts": POSTS})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})