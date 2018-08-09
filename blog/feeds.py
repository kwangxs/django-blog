from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Django 简易博客"
    # 通过聚合阅读器跳转到网站的地址
    link = "/"
    description = "Django 博客文章"

    # 聚合器中显示的内容条目
    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body

