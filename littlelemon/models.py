from django.db import models
from datetime import datetime

# Create your models here.
class BookingTable(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField(default=datetime.now().date())
    
    class Meta:
        db_table = 'BookingTable'
        
    
    def __str__(self) -> str:
        return self.name + " : "+str(self.no_of_guests)


class Menu(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    inventory = models.IntegerField()
    class Meta:
        db_table = 'Menu'
        
    
    def __str__(self) -> str:
        return self.title + " : "+str(self.price)