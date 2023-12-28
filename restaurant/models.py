from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    reservation_slot = models.SmallIntegerField(default=2)
    reservation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name