from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('create-post', views.create_post, name="create_post"),
    path('delete-post/<int:post_id>', views.delete_post, name="delete_post"),
    path('user-profile', views.user_profile, name='user_profile'),
    path('post-page/<int:post_id>', views.post_page, name="post_page"),
    path('user-page/<int:user_id>', views.user_page, name="user_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)