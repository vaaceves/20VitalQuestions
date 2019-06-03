from django.contrib import admin
from .models import Profile, Client, License

# Register your models here.
admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(License)
