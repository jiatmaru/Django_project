from django.urls import path
from . import views

urlpatterns = [
    path('secret/', views.secret_page, name='secret'),
]