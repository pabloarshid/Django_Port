from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.

def blog_index(request):
    blogposts = Post.objects.all().order_by('-created_on')
    context = {
        'blogposts': blogposts
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    blogposts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        'category': category,
        'blogposts': blogposts
    }
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    blogpost = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],=
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post = blogpost)
    context = {
        'blogpost': blogpost,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog_detail.html', context)
