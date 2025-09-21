from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the sidebar
    list_filter = ('publication_year', 'author')

    # Enable search functionality
    search_fields = ('title', 'author')
# accounts/admin.py


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
