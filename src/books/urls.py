from django.urls import path
from books import views

urlpatterns = [
    path('book/', views.book_list),
    path('book/<int:pk>/', views.book_detail),
]