from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_blog_page, name='blog_posts'),
    #postdetail url here
    url(r'post/$',  PostForm, name="post_blog"),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
    url(r'post/create', create_post, name='create_post'),
]