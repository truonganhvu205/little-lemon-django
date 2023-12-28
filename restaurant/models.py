from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='')
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_slot = models.SmallIntegerField(default=2)
    reservation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name