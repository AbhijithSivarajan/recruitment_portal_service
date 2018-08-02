from django.conf.urls import include, url
from django.contrib import admin

from recruiter.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^api/v1/applicants/', include('applicant.urls')),
    url(r'^api/v1/organizations/', include('organization.urls')),
    url(r'^api/v1/recruiters/', include('recruiter.urls')),
    url(r'^admin/', admin.site.urls)
]
