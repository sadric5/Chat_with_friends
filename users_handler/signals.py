from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile




@receiver(post_save, sender=User)
def default_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

"""I don't think we need save_default_profile() 
but maybe you'll on your project
for everything work fine without it ."""

# @receiver(post_save, sender=User)
# def save_default_profile(sender, instance, **kwargs):
# 	instance.profile.save()
		