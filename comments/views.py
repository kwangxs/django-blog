from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 用户通过表单提交数据通过post请求
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # 检查到数据合法
        if form.is_valid():
            # 利用表单的数据生成Commnet模型类的实例，不保存
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            # 保存
            comment.save()
            # 重定向到post的详情页，调用get_absolute_url方法
            return redirect(post)

    else:
        comment_list = post.comment_set.all()
        context = {
                       'post': post,
                       'form': form,
                       'comment_list': comment_list
                   }
        return render(request, 'blog/detail.html', context=context)
    # 不是post请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)
