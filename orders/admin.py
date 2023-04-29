from django.contrib import admin
from .models import Order, Article 


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'processed_status', 'created_at')
    list_filter = ('processed_status',)
    search_fields = ('order_number',)
    inlines = [ArticleInline]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):    
    list_display = ('article_name', 'article_price', 'article_quantity', 'article_code', 'order')
    list_filter = ('order__processed_status',)
    search_fields = ('article_name', 'article_code', 'order__order_number')
