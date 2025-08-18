from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="Home"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/", views.PostsView.as_view(), name="posts"),
]
