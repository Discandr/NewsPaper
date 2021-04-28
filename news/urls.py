from django.urls import path
from .views import NewsList, NewsDetail, NewsFiltered, NewsAdd, NewsDelete, NewsEdit, PostDetail
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsFiltered.as_view()),
    path('add/', NewsAdd.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_upd'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_del'),
    path('<int:pk>', PostDetail.as_view(), name='detail'),
    path('login/',
         LoginView.as_view(template_name = 'news/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'news/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'news/signup.html'),
         name='signup'),




]
