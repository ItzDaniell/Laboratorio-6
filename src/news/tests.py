from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Reporter, Article, Tag


class CategoryModelTest(TestCase):
    """Test cases for the Category model"""
    
    def test_category_creation(self):
        """Test creating a category and checking slug generation"""
        category = Category.objects.create(name="Technology")
        self.assertEqual(category.name, "Technology")
        self.assertEqual(category.slug, "technology")
        self.assertEqual(str(category), "Technology")
