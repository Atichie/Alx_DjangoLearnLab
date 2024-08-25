from django.urls import path
from .views import list_books

urlpatterns = [
        path('books/', views.list_books, name='list_books'),
        path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
        path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login')
        path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
        path('register/',views.register, name='register'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
        path('admin/', admin_view, name='admin_view'),
        path('librarian/', librarian_view, name='librarian_view'),
        path('member/', member_view, name='member_view')
]

from django.urls import include, path
urlpatterns = [
        path('relationship_app/', include('relationship_app.urls')),
]

from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
        path('book/add/', add_book, name='add_book'),
        path('book/edit/<int:pk>/', edit_book, name='edit_book'),
        path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]

from django.urls import include, path

urlpatterns = [
        path('relationship_app/', include("add_book/", "edit_book/", "delete_book/")),
]


