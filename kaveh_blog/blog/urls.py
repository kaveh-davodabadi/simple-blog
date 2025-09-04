from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/", views.PostsView.as_view(), name="posts"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
]
