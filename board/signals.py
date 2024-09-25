from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

from .models import Post, UserResponse


@receiver(post_save, sender=Post)
def post_created(instance, created, **kwargs):
    if not created:
        return
    
    emails = User.objects.filter(
        subscriptions_category=instance.category
    ).values_list('email', flat=True) 

    subject = f'Новое объявление в категории {instance.category}'

    text_content = (
        f'Объявление: {instance.title}\n'
        f'Ссылка на объявление: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Объявление: {instance.title}\n'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на объявление</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(pre_save, sender=UserResponse)
def my_handler(sender, instance, created, **kwargs):
    responder = instance.author
    post = instance.title
    if created:
        subject = 'Получен новый отклик!'
        text = f'{post.author.username}, на Ваше объявление откликнулся {responder.username}'
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[post.author.email]
        )
        responses_link = reverse('responses')
        html = (
            f'<b>{responder.username}</b> откликнулся на объявление "{post.title}".'
            f'Принять или отклонить отклик Вы можете по <a href="{responses_link}">ссылке</a>.'
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        subject = 'Отклик отправлен!'
        text = (f'{responder.username}, Вы оставили отклик на объявление "{post.title}". '
                      f'Когда автор объявления примет решение, Вы получите письмо о статусе отклика.')
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[responder.email]
        )
        msg.send()

    if instance.status:
        subject = 'Отклик принят!'
        text = f'Поздравляем! Ваш отклик на объявление "{post.title}" был принят!'
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[responder.email]
        )
        msg.send()       