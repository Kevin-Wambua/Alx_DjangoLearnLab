from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]

# Utility function to check if user is Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Utility function to check if user is Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Utility function to check if user is Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Create your views here.
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView
from .models import Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
