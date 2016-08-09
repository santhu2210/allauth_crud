from django.conf.urls import url, patterns
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^profile2/','allauthapp.views.profile', name ='profile'),
	)