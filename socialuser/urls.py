from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'socialuser/login.html'}, name='socialuser|login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'socialuser/logout.html', 'next_page': '/'}, name='socialuser|logout'),
)

