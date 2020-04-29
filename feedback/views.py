from django.shortcuts import render, get_object_or_404, redirect, reverse
from posts.models import Post
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.


def complete(request, pk=None):
    """Allows the user to leave feedback on the post after purchasing"""

    if request.method == "POST":
        rate_form = FeedbackForm(request.POST, request.FILES)
        if rate_form.is_valid():
            feedback = rate_form.save()
            return render(request, 'complete.html')
    else:
        rate_form = FeedbackForm()
    return render(
        request,
        'feedback.html',
        {'rate_form': rate_form})