# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
import markdown


"""
请使用下方的模板引擎方式。
def index(request):
    return HttpResponse("欢迎访问我的博客首页！")
"""

"""
请使用下方真正的首页视图函数
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
"""


def index(request):
    # post_list = Post.objects.all().order_by('-create_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 每次访问文章时，进入到该视图函数，阅读量 +1
    post.increase_views()
    
    post.body = markdown.markdown(post.body, extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                  ]) 

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
                   'post': post,
                   'form': form,
                   'comment_list': comment_list
               }

    # return render(request, 'blog/detail.html', context={'post': post})
    return render(request, 'blog/detail.html', context=context)


