from django.db import models
from datetime import datetime
import bcrypt
import re

class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors =  {}
        error  = self.fname_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        error  = self.lname_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        error  = self.username_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        error  = self.email_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        error  = self.password_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        error  = self.confirm_validator(postData)
        if len(error) != 0 :
            errors.update(error)
        return errors

    def fname_validator(self,postData):
        errors = {}
        if len(postData['first_name']) == 0 :
            errors['firstname'] = "First name cannot be left blank"
        return errors

    def lname_validator(self,postData):
        errors = {}
        if len(postData['last_name']) == 0:
            errors['lastname'] = "Last name cannot be left blank"
        return errors
            
    def email_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0 :
            errors['email'] = "Email cannot be left blank"
            return errors
        if len(user) != 0 :
            errors['email_unique'] = "User with this e-mail already exist"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_valid'] = "Invalid e-mail address"
        return errors


    def confirm_validator(self,postData):
        errors = {}
        if postData['password']!=postData['confirm']:
            errors['match'] = "Passwords do not match"
        return errors

    def username_validator(self, postData):
        errors = {}
        UN_REGEX = re.compile(r'[a-zA-Z0-9_-]?(\[|\]|\^|\$|\||\*|\+|\?|\(|\)|\{|\}|@|#|%|&|,|;|:|\"|\'|!|=)+[a-zA-Z0-9_-]?')
        user = User.objects.filter(username=postData['username'])
        if len(postData['username']) == 0 :
            errors['username'] = "Username cannot be left blank"
            return errors
        if len(user) != 0:
            errors['user_unique'] = "Username not available"
        else :
            if len(postData['username']) < 4:
                errors['username_len'] = "Username needs to be at least 4 characters"
            if len(postData['username']) > 20:
                errors['username_len'] = "Username cannot exceed 20 characters"
            if UN_REGEX.match(postData['username']):
                errors['username_special'] = "Username cannot contain special characters besides - and _"
        return errors

    def password_validator(self, postData):
        errors = {}
        PW_REGEX1 = re.compile(r'(?=.*[0-9])')
        PW_REGEX2 = re.compile(r'(?=.*[a-z])')
        PW_REGEX3 = re.compile(r'(?=.*[A-Z])')
        if len(postData['password']) == 0 :
            errors['password'] = "Password cannot be left blank"
            return errors
        if len(postData['password']) < 8:
            errors['pw_length'] = "Password needs to be at least 8 characters long"
        if not PW_REGEX1.match(postData['password']):
            errors['pw_num'] = "Password must contain at least one number"
        if not PW_REGEX2.match(postData['password']):
            errors['pw_low'] = "Password must contain at least one lowercase letter"
        if not PW_REGEX3.match(postData['password']):
            errors['pw_up'] = "Password must contain at least one uppercase letter"
        return errors

        
    def login(self, postData, session):
        errors = {}
        user = User.objects.filter(email=postData['email_username'])
        if not user:
            user = User.objects.filter(username=postData['email_username'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(postData['login_pw'].encode(), logged_user.password.encode()):
                session['userid'] = logged_user.id 
                return errors
            else :
                errors['password'] = "Password is incorrect"
                return errors
        errors['user'] = "User not found"
        return errors

    def add_User(self, postData):
        pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=postData['first_name'],
                            last_name=postData['last_name'],
                            username=postData['username'],
                            email=postData['email'],
                            password=pw_hash
        )
        user = User.objects.last()
        return user.id 

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
