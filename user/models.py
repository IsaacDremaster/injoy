from django.db import models
from django.conf import settings
from phone_field import PhoneField


class Users(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='user', null=True)
    first_name = models.CharField('Имя', max_length=150, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True, null=True)
    username = models.CharField('Никнейм', help_text='Придумайте себе никнейм', max_length=30)
    phone = PhoneField('Контактный номер телефона', blank=True, null=True)
    email = models.EmailField('Почта', max_length=200, blank=True, null=True)
    photo = models.ImageField('Изображение', upload_to='user_images/')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Moderators(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='moder', null=True)
    username = models.CharField('Никнейм', help_text='Придумайте никнейм себе', max_length=30)
    first_name = models.CharField('Имя', max_length=150, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True, null=True)
    email = models.EmailField('Почта', max_length=200, blank=True, null=True)
    photo = models.ImageField('Изображение', upload_to='moder_images/')

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
