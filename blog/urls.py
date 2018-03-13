from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_blog_page, name='blog'),
    url(r'post/$',  PostForm, name="post_blog")
]