from django.shortcuts import render
from django.views import View
from blog.models import Post, Comment, Reply, Document

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()[:6]
        context = {"posts": posts}
        return render(request, "blog/index.html", context=context)


def test_static_view(request):
    from django.conf import settings

    context = {
        "STATIC_URL": settings.STATIC_URL,
        "DEBUG": settings.DEBUG,
    }
    return render(request, "blog/test_static.html", context=context)
