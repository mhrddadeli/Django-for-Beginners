from django.urls import path
from .views import BlogListView, BlogDtailView

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("post/<int:pk>/", BlogDtailView.as_view(), name="post_detail"),
]