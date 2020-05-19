from django.db import models
from datetime import datetime
from apps.login_app.models import User
import bcrypt
import re

class CardManager(models.Manager):
    def NameValidator(self, postData):
        errors = {}
        card = Card.objects.filter(name=postData['card_name'])
        account = Account.objects.filter(name=postData['card_name'])
        if len(card) > 0:
            errors['unique'] = "Card name must be unique"
        if len(account) > 0:
            errors['unique'] = "Card name cannot be used for an account"
        if len(postData['card_name']) < 4:
            errors['length'] = "Card name must be 4 characters or longer"
        return errors
    
    def EditNameValidator(self, postData, og_name):
        errors = {}
        card = Card.objects.filter(name=postData['edit_card_name'])
        account = Account.objects.filter(name=postData['edit_card_name'])
        if (len(card) > 0) & (postData['edit_card_name']!=og_name):
            errors['unique'] = "Card name must be unique"
        if len(account) > 0:
            errors['unique'] = "Card name cannot be used for an account"
        if len(postData['edit_card_name']) < 4:
            errors['length'] = "Card name must be 4 characters or longer"
        return errors
    
    def add_Card(self,postData, session_user) :
        if postData['card_balance'] == "":
            balance = 0.00
        else :
            balance = postData['card_balance']
        Card.objects.create(name=postData['card_name'], balance=balance,user=session_user)

class AccountManager(models.Manager):
    def NameValidator(self, postData):
        errors = {}
        account = Account.objects.filter(name=postData['account_name'])
        card = Card.objects.filter(name=postData['account_name'])
        if len(account) > 0:
            errors['unique'] = "Account name must be unique"
        if len(card) > 0:
            errors['unique'] = "Account name cannot be used for a card"
        if len(postData['account_name']) < 4:
            errors['length'] = "Account name must be 4 characters or longer"
        return errors
        
    def EditNameValidator(self, postData, og_name):
        errors = {}
        card = Card.objects.filter(name=postData['edit_account_name'])
        account = Account.objects.filter(name=postData['edit_account_name'])
        if (len(card) > 0) & (postData['edit_account_name']!=og_name):
            errors['unique'] = "Account name must be unique"
        if len(account) > 0:
            errors['unique'] = "Account name cannot be used for an account"
        if len(postData['edit_account_name']) < 4:
            errors['length'] = "Account name must be 4 characters or longer"
        return errors
    
    def add_Account(self,postData, session_user) :
        if postData['account_balance'] == "":
            balance = 0.00
        else :
            balance = postData['account_balance']
        Account.objects.create(name=postData['account_name'], balance=balance,user=session_user)


class Card(models.Model):
    name = models.CharField(max_length = 255)
    balance = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0.00)
    user = models.ForeignKey(User, related_name="cards")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CardManager()

class Account(models.Model):
    name = models.CharField(max_length = 255)
    balance = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0.00)
    user = models.ForeignKey(User, related_name="accounts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AccountManager()

class Transaction(models.Model) :
    desc = models.CharField(max_length = 255)
    amount = models.DecimalField(max_digits = 15, decimal_places = 2)
    t_type = models.CharField(max_length = 15)
    account_to = models.CharField(max_length = 255, default = None, null=True)
    card_to = models.CharField(max_length = 255, default = None, null=True)
    account_from = models.CharField(max_length = 255, default = None, null=True)
    card_from = models.CharField(max_length = 255, default = None, null=True)
    user = models.ForeignKey(User, related_name="transactions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

