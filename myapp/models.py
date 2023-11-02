from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.phone}"