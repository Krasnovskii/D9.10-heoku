from app.views import PostList, PostDetail, User
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('categories/', PostList.as_view(), name='post-list'),
    path('categories/<int:pk>/', PostDetail.as_view(), name='post-detail'),

]