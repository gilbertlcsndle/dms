from django.conf.urls import url
from .views import (
    CollectionIndex,
    CollectionPrint, 
    CollectionUpdate,
    ParticularIndex,
    get_particular_amount,
    ParticularUpdate,
    ParticularDelete
)

app_name = 'collectionsdeposits'

urlpatterns = [
    url(r'^$', CollectionIndex.as_view(), name='index'),
    url(r'^print/$', CollectionPrint.as_view(), name='print'),
    url(r'^(?P<pk>[0-9]+)/edit/$', CollectionUpdate.as_view(), name='edit'),

    url(r'^particulars/$', ParticularIndex.as_view(), name='particulars'),   
    url(r'^particular-amount/$', get_particular_amount, name='particular-amount'),
    url(r'^(?P<pk>[0-9]+)/particulars/edit/$', ParticularUpdate.as_view(), name='particulars-edit'),
    url(r'^(?P<pk>[0-9]+)/particulars/delete/$', ParticularDelete.as_view(), name='particulars-delete')
]