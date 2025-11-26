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
