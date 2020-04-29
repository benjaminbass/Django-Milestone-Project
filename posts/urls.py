from django.conf.urls import url
from .views import all_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^$', all_posts, name='posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name="post_detail"),
    url(r'^new/$', create_or_edit_post, name="add_post"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name="edit_post"),
]
