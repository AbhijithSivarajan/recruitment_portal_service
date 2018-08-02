from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins

from recruiter.models import Recruiter
from recruiter.serializers import RecruiterSerializer


class RecruiterCollection(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):

    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecruiterMember(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def index(request):
    return HttpResponse("<h1 align=center> Welcome to Recruitment Portal System </h1>")
