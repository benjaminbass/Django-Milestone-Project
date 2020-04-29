from django.conf.urls import url
from .views import complete

urlpatterns = [
    url(r'^$', complete, name='complete')
]