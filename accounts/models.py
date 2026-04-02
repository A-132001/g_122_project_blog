from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    bio = models.TextField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return f"This profile to user {self.user.username}"
    
    

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
    else:
        instance.profile.save()