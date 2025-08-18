from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from blog.models import Post, Comment, Reply, Document
from blog.forms import CommentForm

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()[:6]
        context = {"posts": posts}
        return render(request, "blog/index.html", context=context)


class PostsView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by("-published_at")


class PostDetailView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        comments = Comment.objects.filter(post=post, is_approved=True)
        comment_form = CommentForm()
        context = {"post": post, "comments": comments, "comment_form": comment_form}
        return render(request, "blog/post_detail.html", context=context)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.is_approved = False  # Admin must approve
            new_comment.save()
            return redirect("post_detail", pk=post.pk)
        comments = Comment.objects.filter(post=post, is_approved=True)
        context = {"post": post, "comments": comments, "comment_form": comment_form}
        return render(request, "blog/post_detail.html", context=context)
