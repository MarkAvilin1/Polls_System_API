from django.conf.urls import url
from pollApp import views

urlpatterns = [
    url(r'^api/pc$', views.poll_create),
    url(r'^api/pu/(?P<pk>[0-9]+)$', views.poll_update),
    url(r'^api/qc$', views.question_create),
    url(r'^api/qu/(?P<pk>[0-9]+)$', views.question_update),
    url(r'^api/chc$', views.choice_create),
    url(r'^api/chu/(?P<pk>[0-9]+)$', views.choice_update),
    url(r'^api/ac$', views.answer_create),
    url(r'^api/au/(?P<pk>[0-9]+)$', views.answer_update),
]