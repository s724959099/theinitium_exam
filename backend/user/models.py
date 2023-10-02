from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_employee = models.BooleanField(default=False)


# noinspection PyUnusedLocal
@receiver(signals.post_save, sender=User)
def update_profile(sender, created, instance: User, **kwargs):
    if created:
        Profile.objects.create(user=instance, is_employee=instance.is_staff)
    return instance
