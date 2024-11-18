from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    #path('', views.index),
    # 여기에 URL 패턴을 추가하세요
]