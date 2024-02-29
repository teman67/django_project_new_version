from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # queryset = Post.objects.filter(author=2)
    # queryset = Post.objects.all().order_by("-create_on")
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1)
    # template = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6
