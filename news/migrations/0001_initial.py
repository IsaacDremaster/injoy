# Generated by Django 3.2.3 on 2021-07-07 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('rating', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Рейтинг')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images', verbose_name='Картинки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_owner', to='user.users')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='news_images', verbose_name='Фото')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_images', to='news.news')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_likes', to='news.news')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_likes', to='user.users')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comment', to='news.news')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='user.users')),
            ],
        ),
    ]
