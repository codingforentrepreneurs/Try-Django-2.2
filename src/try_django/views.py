from django.http import HttpResponse
from django.shortcuts import render

# Dont Repeat Yourself = DRY

def home_page(request):
    my_title = "Hello there...."
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return render(request, "hello_world.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "About"})



def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact us"})