from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
        path('<int:pk>/', views.single_post_page),
        path('blog/', views.blog, name='blog'),
        path('', views.index, name='index'),
        path('naverblog/', views.naverblog, name='naverblog'),
        path('aboutme/', views.about_me, name='about_me'),
        path('armylife/', views.army_life, name='army_life'),


]


