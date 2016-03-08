from django.conf.urls import patterns, url
from test_regio_app import views

urlpatterns = patterns('',
    url(r'^landing_page', views.user_form_view, name='user_form_view'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_profile_view, name='delete_view'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update_profile_view, name='update_view'),
    )
