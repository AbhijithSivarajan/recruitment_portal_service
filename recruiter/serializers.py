from rest_framework import serializers
from recruiter.models import Recruiter


class RecruiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recruiter
        fields = ('id', 'name', 'email_id', 'phone_no', 'organization_id')
