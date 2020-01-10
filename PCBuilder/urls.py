from django.urls import path
from PCBuilder import views

urlpatterns = [
    path('builder/', views.builder, name="builder"),
]
