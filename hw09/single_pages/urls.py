from django.urls import path
from . import views
app_name = "single_pages"
urlpatterns = [
    path('About me/', views.about_me, name='about_me'),
    path('NaverBlog/', views.naverblog, name='naverblog'),
    path('Blog/', views.blog, name='blog'),
    path('Armylife/', views.army_life, name='army_life'),
    path('', views.landing, name='landing'),
]