from rest_framework.authtoken import serializers

from app.models import Post, Category


class CategorySerializer(object):
    pass


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'name', 'slug',
                  'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parental_category']
