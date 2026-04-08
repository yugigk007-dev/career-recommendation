from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('create-admin/', views.create_admin),  # 👈 ADD HERE
]