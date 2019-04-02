from django.shortcuts import render

# Create your views here.
from .models import BlogPost



def blog_post_detail_page(request):
    obj = BlogPost.objects.get(id=3)
    template_name = 'blog_post_detail.html'
    context = {"object": obj} # {"title": obj.title}
    return render(request, template_name, context)