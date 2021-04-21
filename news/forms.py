from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_fields = BooleanField(label = 'Проверка')

    class Meta:
        model = Post
        fields = ['post_auth', 'post_type', 'post_had', 'post_text']