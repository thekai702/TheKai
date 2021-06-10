from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)

class Subscriberlist(models.Model):
    email = models.CharField(max_length=255)