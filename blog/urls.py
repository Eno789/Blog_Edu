from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("main/", views.index, name = "index"),
    path("post_new/", views.post_new, name="post_new"),
    path("post/<int:pk>/", views.post_detail, name = "post_detail"),
    path('post/<int:pk>/comment/new', views.comment_new, name = "comment_new"),
    path('post_edit/<int:pk>/', views.post_edit, name="post_edit"),
    path('post_delete/<int:pk>/', views.post_delete, name = "post_delete"),
]