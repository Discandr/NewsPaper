from django.urls import path
from .views import NewsList, NewsDetail, NewsFiltered, NewsAdd, NewsDelete, NewsEdit, PostDetail

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsFiltered.as_view()),
    path('add/', NewsAdd.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_upd'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_del'),
    path('<int:pk>', PostDetail.as_view(), name='detail'),


]
