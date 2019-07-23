from django.urls import path, include
from . import views

urlpatterns = [
        path('post_new', views.post_new, name='post_new'),
        path('post_save', views.post_save, name='post_save'),
        path('<int:blog_id>', views.post_detail, name='post_detail'),
        path('<int:blog_id>/post_mod', views.post_mod, name='post_mod'),
        path('<int:blog_id>/post_remove', views.post_remove, name='post_remove'),
        path('<int:blog_id>/comment', views.comment_new, name='comment_new'),
        path('<int:blog_id>/comment_save', views.comment_save, name='comment_save'),
        path('<int:comment_id>/comment_remove', views.comment_remove, name='comment_remove'),
        path('<int:comment_id>/comment_approve', views.comment_approve, name='comment_approve'),
        ]

