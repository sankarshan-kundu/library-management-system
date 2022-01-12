from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    # path('<int:book_id>/', views.book, name='book'),
]