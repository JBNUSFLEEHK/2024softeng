from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
        path('blog/', views.blog, name='blog'),
        path('', views.landing, name='landing'),
        path('about_me/', views.about_me, name='about_me'),
        path('armylife/', views.armylife, name='armylife'),
]