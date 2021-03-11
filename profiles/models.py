from django.db import models
from django.contrib.auth.models import User
from . import utils

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.code}'

    def get_recommended_profiles(self):
        profiles = Profile.objects.all()
        my_recs = [profile for profile in profiles if profile.recommended_by == self.user]
        return my_recs

    def save(self, *args, **kwargs):
        if self.code == '':
            code = utils.generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)