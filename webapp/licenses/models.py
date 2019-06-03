from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class User(AbstractUser):
#     license_code = models.CharField(max_length=149, blank=True, null=True, default='GLSvipLicensePRO')
#
#     def post_user_activation(sender, instance, created, **kwargs):
#         license_to_count = instance.license_code
#         license_master = License.object.get(code=license_to_count)
#         licenses_found = User.object.filter(license_code=license_to_count).count()
#         license_master.activated_licenses = int(licenses_found)
#         license_master.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_code = models.CharField(max_length=149, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        license_to_check = instance.license_code
        license_checked = License.objects.get(code=license_to_check)
        if created and license_checked:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        license_to_check = instance.license_code
        license_checked = License.objects.get(code=license_to_check)
        if license_checked:
            instance.profile.save()

    def __str__(self):
        return self.user.username

    def post_profile_activation(sender, instance, created, **kwargs):
        license_to_count = instance.license_code
        license_master = License.objects.get(code=license_to_count)
        licenses_found = Profile.objects.filter(license_code=license_to_count).count()
        license_master.activated_licenses = int(licenses_found)
        license_master.save()


class Client(models.Model):
    country = CountryField()
    name = models.CharField(max_length=149, default='Enterprise Name')
    contact_name = models.CharField(max_length=149, default='Client Name')
    contact_phone = models.CharField(max_length=149, default='Client Phone')
    contact_email = models.EmailField(max_length=149, default='contact@email.com')

    def __str__(self):
        return self.name


class License(models.Model):
    country = CountryField()
    client = models.ForeignKey(Client, related_name='client_license', default=1)
    code = models.CharField(max_length=149, blank=True, null=True)
    total_licenses = models.PositiveSmallIntegerField(default=1)
    activated_licenses = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        display_string = str(self.country) + ' - ' + str(self.client.name) + ' - ' + 'Licenses Activated: ' + str(
            self.activated_licenses) + ' of ' + str(self.total_licenses)
        return display_string


post_save.connect(Profile.post_profile_activation, sender=Profile)
