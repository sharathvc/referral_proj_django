from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    referred_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    referral_credits = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def get_recommended_profiles(self):
        return Profile.objects.filter(referred_by=self.user)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(length=12)
        if self.referred_by is None and self.code:
            try:
                referred_by = Profile.objects.get(code=self.code).user
                self.referred_by = referred_by
                self.referral_credits = 100
                referred_by.profile.referral_credits += 100
                referred_by.profile.save()
            except Profile.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)