from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
    def validate_user(request, postData):
        errors = {}

        #validating name 
        if len(postData['name']) < 3 or postData['name'].isalpha():
            if len(postData['name']) < 3:
                errors['name'] = "Name must contain more than 3 characters."
            if not postData['name'].isalpha():
                errors['name_alpha'] = "Name must contain only characters."

        #validating username 
        if len(postData['username']) < 3 or postData['username'].isalpha():
            if len(postData['username']) < 3:
                errors['username'] = "Username must contain more than 3 characters."
            if not postData['username'].isalpha():
                errors['username_alpha'] = "Username must contain only characters."
        if User.objects.filter(username=postData['username']):
            errors['username'] = "This username already exists."

        #validating email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "This is not a valid email."
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists."

        #validating password
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if postData['password'] != postData['cpassword']:
            errors['cpassword'] = "Passwords must match"
        
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password =  models.CharField(max_length=255)

    objects = UserManager()