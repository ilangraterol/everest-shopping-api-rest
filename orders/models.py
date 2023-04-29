from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    processed_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.order_number

class Article(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='articles')
    article_name = models.CharField(max_length=255)
    article_price = models.DecimalField(max_digits=8, decimal_places=2)
    article_quantity = models.IntegerField()
    article_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.article_name
