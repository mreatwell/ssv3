from django.contrib import admin
from .models import Post, Item, Profile  # Import your models here



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
