from django.db import models
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


        
class Hisab(models.Model):
    p_id = models.CharField(max_length=50, blank=False, null=False, default='abc')
    p_type = models.CharField(max_length=50, blank=False, null=False, default='abc')
    p_name = models.CharField(max_length=50, blank=False, null=False, default='abc')
    price = models.IntegerField(blank=False, null=False, default='11')
    quantity = models.IntegerField(blank=False, null=False, default='11')
    image = models.ImageField( upload_to = 'photo/',  blank=False, null=False)#,
    def __str__(self):
        return str(self.id)
        

