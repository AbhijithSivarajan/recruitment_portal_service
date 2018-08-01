from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


def validate_phone_number(phone_number):
    if len(str(phone_number)) != 10:
        raise ValidationError("Phone number {} is not valid".format(phone_number))


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    experience = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=70)
    phone_no = models.BigIntegerField(validators=[validate_phone_number])
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female'),), max_length = 10)
    education = models.CharField(max_length=250)
    current_location = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.name, self.email_id)
