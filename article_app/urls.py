from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<article_id>', views.article, name='article'),
    path('article/<article_id>/comment', views.add_comment, name='add-comment')
]