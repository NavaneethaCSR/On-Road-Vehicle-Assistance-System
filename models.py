from django.db import models


class Mechanics(models.Model):

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

def __str__(self):
        return self.username

class Users(models.Model):

    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)


