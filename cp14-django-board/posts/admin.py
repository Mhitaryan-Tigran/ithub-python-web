from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "contact", "created")
    list_filter = ("category",)
    search_fields = ("title", "text")
