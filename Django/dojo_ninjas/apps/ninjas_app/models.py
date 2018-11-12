from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=25)
    desc = models.TextField()

class Ninja(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dojo = models.ForeignKey (Dojo, related_name="students", on_delete=models.CASCADE)