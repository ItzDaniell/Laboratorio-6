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

class ReporterModelTest(TestCase):
    """Test cases for the Reporter model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="testpassword"
        )
    
    def test_reporter_creation(self):
        """Test creating a reporter profile"""
        reporter = Reporter.objects.create(
            user=self.user,
            bio="Test reporter bio"
        )
        self.assertEqual(str(reporter), "Test User")
        self.assertEqual(reporter.bio, "Test reporter bio")

