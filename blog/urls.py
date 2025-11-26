from django.urls import path

from . import views

app_name = "blog"  # Namespace for URL names


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article-list"),
    path("article/new/", views.ArticleCreateView.as_view(), name="article-create"),
    # path("detail/<int:pk>/", views.article_detail, name="article_detail"),
    path(
        "article/detail/<int:pk>/",
        views.ArticleDetailView.as_view(),
        name="article-detail",
    ),
    path(
        "article/update/<int:pk>/",
        views.ArticleUpdateView.as_view(),
        name="article-update",
    ),
    path(
        "article/delete/<int:pk>/",
        views.ArticleDeleteView.as_view(),
        name="article-delete",
    ),
]
