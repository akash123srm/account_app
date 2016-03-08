from django.conf.urls import patterns, url
from test_regio_app import views

urlpatterns = patterns('',
    url(r'^landing_page', views.user_form_view, name='user_form_view'),
    )
