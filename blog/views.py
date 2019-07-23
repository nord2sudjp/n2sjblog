from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.http import HttpResponse
from django.utils import timezone
def home(request):
    posts = Post.objects.order_by('pk').reverse()
    return render(request, 'blog/home.html', {'posts':posts})

def post_detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    # return HttpResponse("post new")
    return render(request, 'blog/post_new.html')

def post_save(request):
  if request.method == 'POST':
    action = request.POST['action']
    if request.POST['title'] and request.POST['body'] and request.POST['author']:
        w_date = timezone.datetime.now()
        if action == 'add':
           post = Post()
           post.create_date = w_date
        else:
           post = get_object_or_404(Post, pk=request.POST['blog_id'])
        post.title = request.POST['title']
        post.text = request.POST['body']
        post.published_date = w_date
        post.author = request.user
        #post.author = request.POST['author']
        post.save()

        return redirect('post_detail', blog_id=str(post.id))
    else:
        post = Post()
        post.title = request.POST['title']
        post.text = request.POST['body']
        return render(request, request.POST['error_return'],{'error':'All fields are required.', 'post':post})
        #return render(request, 'blog/post_new.html',{'error':'All fields are required.'})
  else:
    return render(request, request.POST['error_return'])

def post_mod(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/post_mod.html', {'post':post})


def post_remove(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    post.delete()
    return redirect('home')

def comment_new(request, blog_id):
    return render(request, 'blog/comment_new.html' , {'blog_id':blog_id})

def comment_save(request, blog_id):
    if request.POST['body']:
        comment = Comment()
        comment.post = get_object_or_404(Post, pk=blog_id)
        if request.user.is_anonymous:
            request.user = None
        comment.author = request.user
        comment.title = request.POST['title']
        comment.text = request.POST['body']
        comment.create_date = timezone.datetime.now()
        comment.save()
    return redirect('post_detail', blog_id=str(blog_id))

def comment_remove(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    return redirect('post_detail', blog_id=str(post.pk))

def comment_approve(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.approve()

    return redirect('post_detail', blog_id=str(comment.post.pk))

