from django.conf.urls import url
from .views import MapIndex

app_name = 'maps'

urlpatterns = [
    url(r'^$', MapIndex.as_view(), name='index'),
]