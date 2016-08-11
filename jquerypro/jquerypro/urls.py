from django.conf.urls import patterns, include, url

from django.contrib import admin
from jqueryapp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jquerypro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^insert/',views.insert , name = 'insert'),
    url(r'^disp/',views.disp, name = 'disp'),
    url(r'^get-users/',views.disp1, name = 'disp1')
)
