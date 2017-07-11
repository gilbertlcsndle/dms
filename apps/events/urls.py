from django.conf.urls import url
from .views import EventIndex, EventDelete, EventUpdate, EventDetail

app_name = 'events'

urlpatterns = [
    url(r'^$', EventIndex.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/edit/$', EventUpdate.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', EventDelete.as_view(), name='delete'),
    url(r'^view/$', EventDetail.as_view(), name='view'),
]