from django.core.validators import URLValidator
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    url = models.CharField(max_length=100, validators=[URLValidator()])
    email_id = models.EmailField(max_length=70)

    def __str__(self):
        return "{} - {}".format(self.name, self.url)
