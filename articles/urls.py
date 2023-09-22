from django.urls import include, path

from articles import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:article_id>/', views.article_view, name='article_view'),
]
