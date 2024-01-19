from django.db import models
from django.forms import ModelForm


class Create(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        db_table = "Create"
