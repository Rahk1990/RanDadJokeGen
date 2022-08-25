from django.urls import path, include
from jokes import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_jokes),
    path('all/', views.get_all_jokes),
]
