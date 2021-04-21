from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_time': ['gt'],
            'post_auth__auth__username': ['icontains'],
        }
#
