from django.conf.urls import url
from .views import (
    ResidentIndex, 
    ResidentUpdate,
    ResidentCreate,
    ResidentDetail,
    get_resident_names,
)

app_name = 'residents'

urlpatterns = [
    url(r'^$', ResidentIndex.as_view(), name='index'),
    url(r'^add/$', ResidentCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', ResidentUpdate.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/view/$', ResidentDetail.as_view(), name='view'),

    # ajax
    url(r'^names/$', get_resident_names, name='names'),
]