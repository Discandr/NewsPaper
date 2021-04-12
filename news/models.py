from django.db import models
import django.contrib.auth
from django.core.validators import MinValueValidator


# Create your models here.

class Author(models.Model):
    auth_rat = models.IntegerField(default=0)
    auth = models.OneToOneField(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)

    def update_rating(self):
        post_rat = 0
        com_rat = 0
        pst_com_rat = 0

        for p in Post.objects.filter(post_auth=self):
            post_rat += p.auth_rat

            for pc in Comment.objects.filter(comm_post=p.id):
                pst_com_rat += pc.auth_rat

        for uc in Comment.objects.filter(comm_user=self.auth):
            com_rat += uc.auth_rat

        self.auth_rat = post_rat * 3 + pst_com_rat + com_rat
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AC'
    TYPE = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    ]

    post_auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=TYPE)
    post_rat = models.IntegerField(default=0)
    post_had = models.CharField(max_length=255)
    post_text = models.TextField(default='')
    post_time = models.DateTimeField(auto_now_add=True)
    post_cat = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return self.post_had


    def short_text(self):
        return self.post_text[:125] + ('...' if len(self.post_text) > 124 else '')

    def dislike(self):
        self.post_rat -= 1
        self.save()

    def like(self):
        self.post_rat += 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comm_time = models.DateTimeField(auto_now=True)
    comm_rat = models.IntegerField(default=0)
    comm_text = models.TextField(default='')
    comm_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comm_user = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comm_text

    def dislike(self):
        self.comm_rat -= 1
        self.save()

    def like(self):
        self.comm_rat += 1
        self.save()
