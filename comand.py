from django.db import models
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

#User
user_1 = User.objects.create_user(username='MrOne', first_name='Jhon', last_name='Greezly', password='Qazxsw123')
user_2 = User.objects.create_user(username='MrToo', first_name='Ben', last_name='Gun', password='Qwerty123')

#Author
auth_1 = Author.objects.create(author=user_1)
auth_2 = Author.objects.create(author=user_2)

#Category
cat_1 = Category.objects.create(category='Новости')
cat_2 = Category.objects.create(category='Спорт')
cat_3 = Category.objects.create(category='Наука')
cat_4 = Category.objects.create(category='Политика')

#Post
art_1 = Post.objects.create(post_auth=auth_1, post_type='AC', post_had='Title 1', post_text='Text 1')
art_2 = Post.objects.create(post_auth=auth_2, post_type='AC', post_had='Title 1', post_text='Text 1')
news_1 = Post.objects.create(post_auth=auth_1, post_type='NW', post_had='Title 1', post_text='Text 1')


#PostCategory
post1_ac_cat1 = PostCategory.objects.create(post=art_1, category=cat_1)
post1_ac_cat3 = PostCategory.objects.create(post=art_1, category=cat_3)
post2_ac_cat2 = PostCategory.objects.create(post=post_a2, category=cat_2)
post2_ac_cat4 = PostCategory.objects.create(post=post_a2, category=cat_4)
post_nw_cat3 = PostCategory.objects.create(post=post_n1, category=cat_3)
post_nw_cat2 = PostCategory.objects.create(post=post_n1, category=cat_2)


#Comment
com_1 = Comment.objects.create(comm_post=post_a1, comm_user=user1, comm_text='всё не то')
com_2 = Comment.objects.create(comm_post=post_a1, comm_user=user2, comm_text='моя не понимать')
com_3 = Comment.objects.create(comm_post=post_a2, comm_user=user2, comm_text='супер гут!')
com_4 = Comment.objects.create(comm_post=post_n1, comm_user=user1, comm_text='можно и лучше')
com_5 = Comment.objects.create(comm_post=post_n1, comm_user=user2, comm_text='я доволен')

# like
art_1.like()
art_2.like()
news_1.like()
art_1.dislike()
art_2.dislike()
news_1.dislike()
com_1.like()
com_2.dislike()
com_3.like()
com_4.dislike()


#rating
auth_1.update_rating()
auth_2.update_rating()

#the best
Author.objects.all().order_by('-auth_rat').values('author__username', 'auth_rat')[0]

# dataview
Post.objects.filter(post_type=Post.ARTICLE).order_by('-auth_rat').values('post_time', 'post_auth__author__username',
                                                                         'post_rat', 'post_head'
                                                                         )[0]
Post.objects.filter(post_type=Post.ARTICLE).order_by('-auth_rat')[0].priview()

# comments
Comment.objects.filter(comm_post=Post.objects.filter(post_type=Post.ARTICLE).order_by('-auth_rat')[0]).values('post_time', 'user', 'post_rat', 'post_text')