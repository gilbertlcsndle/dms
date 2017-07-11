from django.conf.urls import url
from .views import (
    OfficialIndex, 
    OfficialCreate, 
    OfficialUpdate,
)

app_name = 'officials'

urlpatterns = [
    url(r'^$', OfficialIndex.as_view(), name='index'),
    url(r'^add/$', OfficialCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', OfficialUpdate.as_view(), name='edit'),
]