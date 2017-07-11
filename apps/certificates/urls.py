from django.conf.urls import url
from .views import CertificateIndex

app_name = 'certificates'

urlpatterns = [
    url(r'^$', CertificateIndex.as_view(), name='index'),
]