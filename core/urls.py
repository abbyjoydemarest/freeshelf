from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('category/<slug:slug>', views.CategoryListView.as_view(), name='category-list'),
    path('accounts/', include('registration.backends.default.urls')),
]
