from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('create_post', views.create_post, name="create_post"),
    path('user_profile', views.user_profile, name='user_profile'),
    path('post_page/<int:post_id>', views.post_page, name="post_page")
]