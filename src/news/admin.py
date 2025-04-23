from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Reporter, Article, Tag

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for categories"""
    list_display = ("name", "slug", "article_count")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
    
    def article_count(self, obj):
        """Count articles in this category"""
        count = obj.articles.count()
        return count if count > 0 else "-"
    article_count.short_description = "Articles"

