from django.urls import path
from django.conf.urls.static import static
from News.views import HomeView, NewsByCategory, ViewNews, AddNews, user_login, user_logout
#RegisterView
from django.views.decorators.cache import cache_page
from django.conf import settings

urlpatterns = [
    path('', cache_page(30)(HomeView.as_view()), name='Home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('news/<int:news_id>', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    #path('register', , name='Register'),
    path('login', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
