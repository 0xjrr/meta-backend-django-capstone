from django.db import models

# Create your models here.

class Menu(models.Model):
    tittle = models.CharField(max_length=255, null=False)
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    iventory = models.IntegerField(default=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return self.tittle

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name