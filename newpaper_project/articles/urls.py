from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path("new/", ArticleCreateView.as_view(), name="articles_new"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="articles_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="articles_update"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="articles_delete"),
]
