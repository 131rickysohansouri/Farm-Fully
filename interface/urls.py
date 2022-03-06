from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='Farmfully-home'),
    path('forums/', views.forums,name='Forums'),
    path('learning/', views.learning,name='E-learning'),
]
