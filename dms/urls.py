from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from apps.users.views import ForgotPassword, get_security_info

from .forms import LoginForm
from .views import Index, Dashboard, EventList, FileDelete, FileCreate

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),

    # users
    url(r'^forgot-pass/$', ForgotPassword.as_view(), name='forgot-pass'),
    url(r'^security-info/$', get_security_info, name='security-info'),
    
    # files
    url(r'^files/(?P<pk>[0-9]+)/delete/$', FileDelete.as_view(), name='files-delete'),
    url(r'^files/add/$', FileCreate.as_view(), name='files-add'),
    # events   
    url(r'^events/list/$', EventList.as_view(), name='event-list'),
    
    # auth
    url(r'^login/', auth_views.login, {
        'template_name': 'login.html', 
        'authentication_form': LoginForm
    }, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

    # ajax request

    # apps
    url(r'^officials/', include('apps.officials.urls')),
    url(r'^events/', include('apps.events.urls')),
    url(r'^certificates/', include('apps.certificates.urls')),
    url(r'^residents/', include('apps.residents.urls')),
    url(r'^collections/', include('apps.collectionsdeposits.urls')),
    url(r'^attendance/', include('apps.attendance.urls')),
    url(r'^maps/', include('apps.maps.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
