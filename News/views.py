from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .models import News, Category
from .utils import MyMixin


# Create your views here.

class RegisterView(CreateView):
    template_name = 'News/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('Login')

def MyView(req):
    return render(req, 'news/dist/index.html')


# def register(req):
#     if req.method == 'POST':
#         form = UserCreationForm()
#         if form.is_valid():
#             form.save()
#             messages.sucess(req, 'Регистрация прошла успешно')
#             return redirect('login')
#         else:
#             messages.error(req, 'Error registration')
#     else:
#         form = UserCreationForm()
#     return render(req, 'News/register.html', {'form': form})

def user_logout(req):
    logout(req)
    return redirect('Login')


def user_login(req):
    if req.method == 'POST':
        form = UserLoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(req, 'News/login.html', {'form': form})


class HomeView(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': 'Главная'}
    mixin_group = 'hello world'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_group'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'

# def view_news(req, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     ctx = {'news_item': news_item}
#     return render(req, 'news/view_news.html', context=ctx)


# def get_category(req, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     ctx = {'news': news, 'categories': categories, 'category': category}
#     return render(req, 'News/category.html', context=ctx)


# def add_news(req):
#     if req.method == 'POST':
#         form = NewsForm(req.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm
#         return render(req, 'News/add_news.html', {'form': form})

# def index(req):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     ctx = {'news': news, 'title': 'Список новостей', 'categories': categories}
#     return render(req, 'News/index.html', context=ctx)

# def test(req):
#     objects = ['john', 'paul', 'george', 'ringo', 'john2', 'paul2', 'george2', 'ringo2']
#     paginator = Paginator(objects, 2)
#     page_num = req.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(req, 'News/test.html', {'page_obj': page_objects})
