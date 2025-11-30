import logging

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import ArticleSerializer

logger = logging.getLogger(__name__)

from .forms import ArticleForm
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by("-published_date")
    context = {"object_list": articles}
    return render(request, "blog/article_list.html", context)


def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        article = Article.objects.create(
            title=title, content=content, author=request.user
        )
        return redirect("blog:article_detail", pk=article.id)

    return render(request, "blog/create_article.html")


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "blog/article_detail.html", {"article": article})


class ArticleListView(ListView):
    model = Article
    # # template_name = 'blog/article_list.html'
    # # context_object_name = "articles"
    # paginate_by = 10
    # ordering = ["-published_date"]

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    # template_name = "blog/article_form.html"
    success_url = reverse_lazy("blog:article-list")

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"/admin/login/?next={request.path}")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):

        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            logger.warning("WARNING: User is not authenticated, author will be None")

        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    # template_name = "blog/article_form.html"
    success_url = reverse_lazy("blog:article-list")

    def form_valid(self, form):
        if not self.request.user.is_anonymous:
            form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ArticleDetailView(DetailView):
    model = Article
    # template_name = "blog/article_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article-list")


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = []

    def get_permissions(self):
        """
        Custom permissions:
        - List view is open to everyone
        - Other operations require authentication
        """
        if self.action == "list":
            permission_classes = []  # No authentication required for list
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # def perform_create(self, serializer):
    #     """Automatically set the author to the current user"""
    #     serializer.save(author=self.request.user)

    # def update(self, request, *args, **kwargs):
    #     """Only allow author to update their own blog"""
    #     blog = self.get_object()
    #     if blog.author != request.user:
    #         return Response(
    #             {"error": "You can only update your own blogs"},
    #             status=status.HTTP_403_FORBIDDEN,
    #         )
    #     return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     """Only allow author to delete their own blog"""
    #     blog = self.get_object()
    #     if blog.author != request.user:
    #         return Response(
    #             {"error": "You can only delete your own blogs"},
    #             status=status.HTTP_403_FORBIDDEN,
    #         )
    #     return super().destroy(request, *args, **kwargs)
