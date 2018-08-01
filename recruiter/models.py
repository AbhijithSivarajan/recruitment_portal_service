from django.core.exceptions import ValidationError
from django.db import models

from organization.models import Organization


def validate_phone_number(phone_number):
    if len(str(phone_number)) != 10:
        raise ValidationError("Phone number {} is not valid".format(phone_number))


class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=70)
    phone_no = models.BigIntegerField(validators=[validate_phone_number])
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, 
                                        related_name='recruiter')

    def __str__(self):
        return "{} - {}".format(self.name, self.email_id)
