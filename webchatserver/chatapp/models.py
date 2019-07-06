from django.db import models


class Message(models.Model):

    origin = models.CharField(max_length=25)
    destination = models.CharField(max_length=25)
    text = models.CharField(max_length=255, default="")
    date = models.DateTimeField()

    def __str__(self):
        return self.origin + " " + self.destination + " " + self.text

