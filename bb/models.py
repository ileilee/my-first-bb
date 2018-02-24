from django.db import models


class Customer(models.Model):
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    organization = models.CharField(max_length=100, blank=True)


    def create(self):
        self.save()

    def __str__(self):
        return self.phone
