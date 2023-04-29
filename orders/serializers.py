from rest_framework import serializers
from .models import Order, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'article_name', 'article_price', 'article_quantity', 'article_code')

class OrderSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'order_number', 'processed_status', 'articles')

    def create(self, validated_data):
        articles_data = validated_data.pop('articles')
        order = Order.objects.create(**validated_data)
        for article_data in articles_data:
            Article.objects.create(order=order, **article_data)
        return order
