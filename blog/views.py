from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Like
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
       comment_form = CommentForm(data=request.POST)
       if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )

    comment_form = CommentForm()


    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
        )

@login_required
def toggle_like(request, post_id):
    """
    Toggle like or unlike on a specific post for the logged-in user.
    """
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        # If the like already exists, delete it (unlike the post)
        like.delete()
        liked = False
    else:
        # If the like does not exist, create it (like the post)
        liked = True

    # Calculate total likes for the post
    total_likes = post.likes.count()

    # Return the new like status and total likes as JSON (for AJAX use)
    return JsonResponse({'liked': liked, 'total_likes': total_likes})  