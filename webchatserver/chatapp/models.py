from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    origin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="src")
    destination = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dest", null=True, blank=True)
    text = models.TextField(default="")
    date = models.DateTimeField()

    def __str__(self):
        return str(self.text)

