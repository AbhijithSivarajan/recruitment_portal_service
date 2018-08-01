from rest_framework import serializers
from applicant.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ('id', 'name', 'date_of_birth', 'experience', 'email_id',
                  'phone_no', 'gender', 'education', 'current_location')
