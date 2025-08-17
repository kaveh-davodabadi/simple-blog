from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="Home"),
    path("test-static/", views.test_static_view, name="test_static"),
]
