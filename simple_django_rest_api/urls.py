from django.conf.urls import patterns, include, url
from django.contrib import admin
from time_now.views import TimeNowView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_django_rest_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^now/', TimeNowView.as_view(), name='time_now_view'),
    url(r'^admin/', include(admin.site.urls)),
    
)
