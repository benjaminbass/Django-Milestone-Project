from django import forms
from .models import Post


class RentPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'service_name',
            'description',
            'name',
            'price',
            'deadline',
            'tag',
            'image',
            'published_date')
