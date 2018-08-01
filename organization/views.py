from rest_framework import generics
from rest_framework import mixins

from organization.models import Organization
from organization.serializers import OrganizationSerializer



class OrganizationCollection(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrganizationMember(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
