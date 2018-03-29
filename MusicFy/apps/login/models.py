from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class UserManager(models.Manager):
    def validate_user(request, postData):
        errors = {}

        #validating first_name 
        if len(postData['first_name']) < 3 or postData['first_name'].isalpha():
            if len(postData['first_name']) < 3:
                errors['name'] = "Name must contain more than 3 characters."
            if not postData['first_name'].isalpha():
                errors['name_alpha'] = "Name must contain only characters."
        #validating last_name
        if len(postData['last_name']) < 3 or postData['last_name'].isalpha():
            if len(postData['last_name']) < 3:
                errors['name'] = "Name must contain more than 3 characters."
            if not postData['last_name'].isalpha():
                errors['name_alpha'] = "Name must contain only characters."

        #validating username 
        if len(postData['email']) < 3 or postData['email'].isalpha():
            if len(postData['email']) < 3:
                errors['username'] = "Username must contain more than 3 characters."
            if not postData['email'].isalpha():
                errors['username_alpha'] = "Username must contain only characters."
        if User.objects.filter(email=postData['email']):
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #birthday = models.DateTimeField(auto_now=False, auto_now_add=False )
    #gender =  models.CharField(max_length=255)
    password =  models.CharField(max_length=255)

    objects = UserManager()