from django.shortcuts import render
from ...models.models import Post


def show(request):
    posts = Post.objects.all()
    return render(request, 'catalog/catalog.html', {'posts': posts})
