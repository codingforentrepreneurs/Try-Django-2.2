from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


# GET -> 1 object
# filter -> [] objects

def blog_post_detail_page(request, slug):
    print("DJANGO SAYS", request.method, request.path, request.user)
    # obj = BlogPost.objects.get(slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404       
    # obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj} # {"title": obj.title}
    return render(request, template_name, context)


# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / DELETE

# Create Retrieve Update Delete











