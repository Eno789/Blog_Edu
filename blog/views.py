from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post, Comment
from blog.forms import PostForm, CommentForm

@login_required
def index(request):
    if Post.objects.filter(author_id=request.user):
        post_list = Post.objects.all()
    else:
        post_list = Post.objects.filter(publish=True)
    comment_form = CommentForm

    return render(request, 'blog/index.html',
                  {
                      "post_list" : post_list,
                      "comment_form" : comment_form,
                  })
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm
    return render(request, 'blog/post_detail.html',
                  {
                      "post": post,
                      "comment_form": comment_form,
                  })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "포스팅 생성성공")
            return redirect("blog:index")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html",
                  {
                      "form" : form
                  })

def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method== "POST":
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                return render(request, "_comment.html",
                              {
                                  "comment" : comment,
                              })
            return redirect("blog:index")
    else:
        form = CommentForm()
    return render(request, "blog/comment_form.html",
                  {
                      "form" : form,
                  })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, "Error")
        return redirect("blog:index")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.now()
            post.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html",
                  {
                      "post" : post,
                  })
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect("blog:index")
    else:
        messages.error(request, "Error!")
    return redirect("blog:index")






























