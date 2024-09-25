from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField



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
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text=RichTextUploadingField(verbose_name='Текст', config_name='extends', null=True, blank=True)
    category = models.ManyToManyField(Category, through= 'PostCategory', verbose_name='Категория')
    media = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, blank= True)
    post_category = models.ForeignKey(Category, on_delete= models.CASCADE, blank= True)       


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category_sub = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор отклика')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False, verbose_name='Статус')
    # date_reply = models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')

    def __str__(self):
        return f'{self.author}: {self.text}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'