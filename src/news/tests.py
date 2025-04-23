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

class ArticleModelTest(TestCase):
    """Test cases for the Article model"""
    
    def setUp(self):
        """Set up test data"""
        # Create user and reporter
        self.user = User.objects.create_user(
            username="reporter",
            first_name="Jane",
            last_name="Doe",
            password="password123"
        )
        self.reporter = Reporter.objects.create(user=self.user)
        
        # Create category
        self.category = Category.objects.create(name="Sports")
        
        # Create tags
        self.tag1 = Tag.objects.create(name="Football")
        self.tag2 = Tag.objects.create(name="World Cup")
    
    def test_article_creation(self):
        """Test creating an article with relationships"""
        article = Article.objects.create(
            title="Test Article",
            content="This is test content for the article.",
            reporter=self.reporter,
            category=self.category,
            status="published"
        )
        
        # Add tags
        article.tags.add(self.tag1, self.tag2)
        
        # Test basic properties
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.slug, "test-article")
        self.assertEqual(str(article), "Test Article")
        
        # Test relationships
        self.assertEqual(article.reporter, self.reporter)
        self.assertEqual(article.category, self.category)
        self.assertEqual(article.tags.count(), 2)
        self.assertTrue(self.tag1 in article.tags.all())
        self.assertTrue(self.tag2 in article.tags.all())
        
        # Test summary generation
        self.assertTrue(article.summary.startswith("This is test content"))

