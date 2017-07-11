from django.conf.urls import url
from .views import AttendanceIndex

app_name = 'attendance'

urlpatterns = [
    url(r'^$', AttendanceIndex.as_view(), name='index'),
]