from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_exam, name='list_exam'),
    path('exam/<int:exam_id>/', views.start_exam, name='start_exam'),
]
