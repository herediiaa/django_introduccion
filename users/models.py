from django.db import models

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
   
   
# Opciones de una campo
STATUS_CHOICE=[
    ('R', 'Reviewed'),
    ('N', 'Not reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted'),
] 

class Website(models.Model):
    
    name = models.CharField(max_length=50) 
    url = models.URLField()
    released_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICE, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
# en la shell
'''
from app.models import Class1, Class2 
import datetime
d = datetime.date(y,m,d)

object = get_field_display wg: get_status_display()

object(key=value) 



'''