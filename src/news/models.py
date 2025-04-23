from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    """Category model for organizing articles"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("news:category_detail", kwargs={"slug": self.slug})
