from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

user = User.objects.get(username='your_superuser_username')
user_profile = user.userprofile
user_profile.role = 'Admin'
user_profile.save()