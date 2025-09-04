from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView
from blog.models import Post, Comment, Reply, Document
from blog.forms import CommentForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


class IndexView(View):
    def get_posts(self):
        return Post.objects.filter(is_published=True)[:4]

    def get(self, request, *args, **kwargs):
        posts = self.get_posts()
        form = ContactForm()
        context = {"posts": posts, "form": form}
        return render(request, "blog/index.html", context=context)

    def post(self, request, *args, **kwargs):
        posts = self.get_posts()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message_content = form.cleaned_data["message_content"]

            send_mail(
                subject=f"mail from {name}",
                message=message_content + email,
                from_email=email,
                recipient_list=["davodabadikaveh@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, "Your message has been received! Thank you 😊")
            form = ContactForm()

        else:
            form = ContactForm()
        return render(request, "blog/index.html", {"form": form, "posts": posts})


class PostsView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by("-published_at")


class PostDetailView(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post, is_approved=True)
        comment_form = CommentForm()
        context = {"post": post, "comments": comments, "comment_form": comment_form}
        return render(request, "blog/post_detail.html", context=context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.is_approved = False  # Admin must approve
            new_comment.save()
            return redirect("post_detail", slug=post.slug)
        comments = Comment.objects.filter(post=post, is_approved=True)
        context = {"post": post, "comments": comments, "comment_form": comment_form}
        return render(request, "blog/post_detail.html", context=context)


class ResumeView(TemplateView):
    template_name = "blog/resume.html"
