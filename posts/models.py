from django.db import models
from django.forms import DateTimeField
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='post'
    name = models.CharField(
        'Name',blank=False,null = False,max_length=14,
        db_index=True,default='Anonymous'
        # name can't be blank or null,default is anonymous if no value is put
        # index true (name will be the index as primary key)
        # index true(if match is found then it will stop searching other wise it will move to the bottom of table even if match is found)
    )
    body = models.CharField(
        'Body',blank=True,null =True,max_length=140, db_index=True)
    created_at = models.DateTimeField(
        'created DateTime',blank=True, auto_now_add=True)
    image = CloudinaryField(
        'image', blank = 'true'
    
    )
    likes = models.PositiveIntegerField(
        'Likes', default=0, null=True, blank=True
    )