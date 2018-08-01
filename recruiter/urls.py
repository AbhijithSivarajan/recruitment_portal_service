from django.conf.urls import url
from recruiter import views


urlpatterns = [
    url(r'^$', views.RecruiterCollection.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.RecruiterMember.as_view())
]
