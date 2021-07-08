from django.db import models
from django.conf import settings


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'post_owner')
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class PostImage(models.Model):
    post = models.ForeignKey('post.Post', models.CASCADE, 'post_image')
    image = models.FileField('Фото/Картинка', upload_to='post_image')


class Comments(models.Model):
    post = models.ForeignKey('post.Post', models.CASCADE, 'post_comment')
    owner = models.ForeignKey('user.Users', models.CASCADE, 'comment_owner')
    text = models.TextField()
    published_date = models.DateTimeField('Дата публикации', auto_now_add=True)
