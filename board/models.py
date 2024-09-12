from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    TYPE = (
        ('Tanks', 'Танки'),
        ('Heals', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guild Masters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potions makers', 'Зельевары'),
        ('Spell masters', 'Мастера заклинаний'),
    )

    name_category = models.CharField(max_length=20, choices=TYPE, default='Tanks', help_text='category')

    def __str__(self):
        return self.name_category
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ManyToManyField(Category, through= 'PostCategory')
    upload = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, blank= True)
    post_category = models.ForeignKey(Category, on_delete= models.CASCADE, blank= True)       


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
