from django.conf.urls import url
from organization import views


urlpatterns = [
    url(r'^$', views.OrganizationCollection.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.OrganizationMember.as_view())
]
