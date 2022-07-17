# we want user profile to be created for each new user

from django.db.models.signals import post_save
#this is the signal that gets fired after the object is saved
from django.contrib.auth.models import User
#user model is sender
from django.dispatch import receiver
from .models import Profile

# when a user is saved then send this signal which will be recieved by reciever(create_profile)
@receiver(post_save,sender=User)
def create_profile(sender, instance, created,**kwargs):
	if created:
		profile.objects.create(user=instance)

def savee_profile(sender, instance,**kwargs):
	instance.profile.save()