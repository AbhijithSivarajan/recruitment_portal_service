from rest_framework import serializers
from organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'name', 'address', 'url', 'email_id')
