from django.db import models

# Create your models here.


class Contacts(models.Model):
    email = models.CharField(max_length=200)
    node_id = models.CharField(max_length=200)
    node_mac = models.CharField(max_length=200)
    gateway_id = models.CharField(max_length=200)
    client_ip = models.CharField(max_length=200)
    client_mac = models.CharField(max_length=200)
    logged_in = models.DateTimeField()
