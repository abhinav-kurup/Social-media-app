from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.CharField(max_length=1000,blank=True)
    profile_image=models.ImageField(upload_to='profile_images',default='team4.jpg')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
