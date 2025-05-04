from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('hi/', views.hi),
    path('whoyouare/', views.whoyouare),
    path('jsonhello', views.jsonhello),
    path('posthello/', views.post_hello)
]

