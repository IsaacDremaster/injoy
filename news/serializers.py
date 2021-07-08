from rest_framework import serializers

from news.models import News, Comments, Likes, NewsImages

from user.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'username', 'photo')


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comments.objects.create(owner=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        data = validated_data.copy()
        data.pop('news', None)
        for attr, value, in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImages
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
    news_image = NewsImageSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True, many=False)
    news_comment = CommentSerializer(many=True, read_only=True)
    likes = serializers.IntegerField()

    class Meta:
        model = News
        fields = ('id', 'owner', 'text', 'image', 'rating', 'created', )

    def create(self, validated_data):
        user = self.context.get('request').user
        news = News.objects.create(owner=user, **validated_data)
        images = self.context.get('request').data.getlist('news_images')
        images_list = [NewsImages(image=item, news=news) for item in images]
        NewsImages.objects.bulk_create(images_list)
        return news

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        images = self.context.get('request').data.getlist('news_images')
        if images:
            NewsImages.objects.filter(news=instance).delete()
            images_list = [NewsImages(image=item, news=instance) for item in images]
            NewsImages.objects.bulk_create(images_list)
        return instance


