from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def register(self, data):
        try:
            self.get(email=data['email'])
            # if there is a user with that email - we can't register the user
            return "failed to register user"
        except:
            # yay register user!
            # User.objects.create = self.create
            user = self.create(name=data['name'], email=data['email'])
            # this create, also returns the create user
            return user

    def login (self, data):
        try:
            user = self.get(email=data['email'])
            return user
        except:
            return "failed to login"

# Create your models here.
#https://docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
