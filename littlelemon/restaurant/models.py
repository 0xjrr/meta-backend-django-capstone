from django.db import models

# Create your models here.

class Menu(models.Model):
    tittle = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    iventory = models.IntegerField(default=0)

    def __str__(self):
        return self.tittle

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name