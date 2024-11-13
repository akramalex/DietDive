from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Check if the user has liked the post
    user_liked = Like.objects.filter(user=request.user, post=post, value='Like').exists()

    # Get the like count
    like_count = Like.objects.filter(post=post, value='Like').count()

    # Handle comment form
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
    else:
        comment_form = CommentForm()

    # Pass like-related data to template
    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "user_liked": user_liked,
        "like_count": like_count,
    })
class PostLike(View):
    """
    Handle the like/unlike functionality for a post.
    """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        # Check if the user has already liked the post
        like_instance = Like.objects.filter(user=request.user, post=post)

        if like_instance.exists():
            # If the user already liked the post, remove the like (unlike)
            like_instance.delete()
        else:
            # If the user has not liked the post, create a new like entry
            Like.objects.create(user=request.user, post=post, value='Like')

        # Redirect back to the post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))