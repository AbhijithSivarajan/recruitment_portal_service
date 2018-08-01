from django.conf.urls import url
from applicant import views


urlpatterns = [
    url(r'^$', views.ApplicantCollection.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ApplicantMember.as_view())
]
