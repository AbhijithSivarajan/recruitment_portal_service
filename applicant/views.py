from rest_framework import generics
from rest_framework import mixins

from applicant.models import Applicant
from applicant.serializers import ApplicantSerializer



class ApplicantCollection(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApplicantMember(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
