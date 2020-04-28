from django.conf.urls import url, include
from .views import all_posts

urlpatterns = [
    url(r'^$', all_posts, name='posts'),

]
