from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    text = models.TextField('Описание')
    owner = models.ForeignKey('user.Users', models.CASCADE, related_name='news_owner')
    rating = models.PositiveSmallIntegerField('Рейтинг', default=0, null=True)
    image = models.ImageField('Картинки', upload_to='news_images', blank=True, null=True)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    news = models.ForeignKey('news.News', models.CASCADE, 'news_images')
    image = models.FileField('Фото', upload_to='news_images')


class Comments(models.Model):
    owner = models.ForeignKey('user.Users', models.CASCADE, 'user_comment')
    news = models.ForeignKey('news.News', models.CASCADE, 'news_comment')
    text = models.TextField('Текст комментария')
    created = models.DateTimeField('Дата комментария', auto_now_add=True)

    def __str__(self):
        return self.text


class Likes(models.Model):
    user = models.ForeignKey('user.Users', models.CASCADE, 'users_likes', null=True)
    news = models.ForeignKey('news.News', models.CASCADE, 'news_likes')
