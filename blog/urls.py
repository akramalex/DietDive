from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/toggle_like/', views.toggle_like, name='toggle_like'),
]