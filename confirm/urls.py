from django.conf.urls import url
from .views import confirm

urlpatterns = [
    url(r'^$', confirm, name='confirm'),
]