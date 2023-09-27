from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('viewnews/', views.viewnews),
    path('contact/', views.contact),
    path('feedback/', views.feedback),
    path('register/', views.register),
    path('profile/', views.profile),
    path('logout/', views.logout),
    path('blog/', views.blog),
    path('shownews/', views.shownews),
    path('detailnews/', views.detailnews),
]