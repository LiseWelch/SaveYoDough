from django.shortcuts import render, redirect
from .models import Card, Account, Transaction
from apps.login_app.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from decimal import *

def root(request) :
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['userid'])
    if 'login_check' in request.session :
        del request.session['login_check']
    context = {
        "user": user,
        "transactions" : user.transactions.all().order_by("-created_at"),
        "accounts" : user.accounts.all(),
        "cards" : user.cards.all()
    }
    return render(request, 'budget_app/root.html', context)

@csrf_exempt
def account_name(request) :
    errors = {}
    if request.method == 'POST':
        errors = Account.objects.NameValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='account_name')
    return render(request, 'budget_app/partials/account_name.html')

@csrf_exempt
def card_name(request) :
    errors = {}
    if request.method == 'POST':
        errors = Card.objects.NameValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='card_name')
    return render(request, 'budget_app/partials/card_name.html')

@csrf_exempt
def edit_card_name(request) :
    errors = {}
    if request.method == 'POST':
        errors = Card.objects.EditNameValidator(request.POST, request.POST.get('c_og_name'))
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='card_name')
    return render(request, 'budget_app/partials/edit_card_name.html')

@csrf_exempt
def edit_account_name(request) :
    errors = {}
    if request.method == 'POST':
        account = Account.objects.get(id=request.POST['account_id'])
        errors = Account.objects.EditNameValidator(request.POST, account.name)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='account_name')
    return render(request, 'budget_app/partials/edit_account_name.html')

@csrf_exempt        
def create_account(request) :
    errors = {}
    error = Account.objects.NameValidator(request.POST)
    if len(error) > 0:
        errors.update(error)
        return render(request, 'budget_app/partials/a_err.html')
    else :
        user = User.objects.get(id=request.session['userid'])
        Account.objects.add_Account(request.POST, user)
        context = {
            "accounts": user.accounts.all()
        }
        return render(request, 'budget_app/partials/added_accounts.html', context)
        
@csrf_exempt        
def create_card(request) :
    errors = {}
    error = Card.objects.NameValidator(request.POST)
    if len(error) > 0:
        errors.update(error)
        return render(request, 'budget_app/partials/c_err.html')
    else :
        user = User.objects.get(id=request.session['userid'])
        Card.objects.add_Card(request.POST, user)
        context = {
            "cards": user.cards.all()
        }
        return render(request, 'budget_app/partials/added_cards.html', context)

@csrf_exempt  
def delete_card(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    user = User.objects.get(id=request.session['userid'])
    context = {
            "cards": user.cards.all()
        }
    return render(request, 'budget_app/partials/added_cards.html', context)
        
@csrf_exempt  
def delete_account(request, id):
    account = Account.objects.get(id=id)
    account.delete()
    user = User.objects.get(id=request.session['userid'])
    context = {
            "accounts": user.accounts.all()
        }
    return render(request, 'budget_app/partials/added_accounts.html', context)

@csrf_exempt  
def delete_tran(request, id):
    tran = Transaction.objects.get(id=id)
    delete_tran_logic(tran)
    user = User.objects.get(id=request.session['userid'])
    context = {
            "transactions": user.transactions.all().order_by("-created_at")
        }
    return render(request, 'budget_app/partials/added_tran.html', context)

def delete_tran_logic(tran):
    if tran.t_type == "deposit":
        account = Account.objects.filter(name=tran.account_to)
        if len(account)>0:
            account[0].balance -= tran.amount
            account[0].save()
    elif tran.t_type == "withdraw":
        account = Account.objects.filter(name=tran.account_to)
        if len(account)>0:
            account[0].balance += tran.amount
            account[0].save()
    elif tran.t_type == "purchase":
        if tran.account_from :
            account = Account.objects.filter(name=tran.account_from)
            if len(account)>0:
                account[0].balance += tran.amount
                account[0].save()
        else :
            card = Card.objects.filter(name=tran.card_from)
            if len(card)>0:
                card[0].balance -= tran.amount
                card[0].save()
    else :
        card = Card.objects.filter(name=tran.card_to)
        if len(card)>0:
            card[0].balance += tran.amount
            card[0].save()
        account = Account.objects.filter(name=tran.account_from)
        if len(account)>0:
            account[0].balance += tran.amount
            account[0].save()
    tran.delete()
    
def add_purchase(request):
    user = User.objects.get(id=request.session['userid'])
    card = user.cards.filter(name=request.POST['on'])
    if len(card) > 0 :
        for c in card :
            c.balance += Decimal(request.POST['amount'])
            c.save()
            Transaction.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], t_type="purchase", card_from=request.POST['on'], user=user)
    else :
        account = user.accounts.filter(name=request.POST["on"])
        for a in account :
            a.balance -= Decimal(request.POST['amount'])
            a.save()
            Transaction.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], t_type="purchase", account_from=request.POST['on'], user=user)
    context = {
        "user": user,
        "transactions" : user.transactions.all().order_by("-created_at"),
        "accounts" : user.accounts.all(),
        "cards" : user.cards.all()
    }
    return render(request, 'budget_app/partials/added_tran.html', context)

def add_deposit(request):
    user = User.objects.get(id=request.session['userid'])
    deposit = user.accounts.get(name=request.POST['to'])
    Transaction.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], t_type="deposit", account_to=request.POST['to'], user=user)
    deposit.balance += Decimal(request.POST['amount'])
    deposit.save()
    context = {
        "user": user,
        "transactions" : user.transactions.all().order_by("-created_at"),
        "accounts" : user.accounts.all(),
        "cards" : user.cards.all()
    }
    return render(request, 'budget_app/partials/added_tran.html', context)

def add_withdraw(request):
    user = User.objects.get(id=request.session['userid'])
    withdraw = user.accounts.get(name=request.POST['from'])
    Transaction.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], t_type="withdraw", account_to=request.POST['from'], user=user)
    withdraw.balance -= Decimal(request.POST['amount'])
    withdraw.save()
    context = {
        "user": user,
        "transactions" : user.transactions.all().order_by("-created_at"),
        "accounts" : user.accounts.all(),
        "cards" : user.cards.all()
    }
    return render(request, 'budget_app/partials/added_tran.html', context)

def add_payment(request):
    user = User.objects.get(id=request.session['userid'])
    card = user.cards.get(name=request.POST['payment_to'])
    account = user.accounts.get(name=request.POST['payment_from'])
    card.balance -= Decimal(request.POST['amount'])
    card.save()
    account.balance -= Decimal(request.POST['amount'])
    account.save()
    Transaction.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], t_type="payment", card_to=request.POST['payment_to'], account_from=request.POST['payment_from'],user=user)
    context = {
        "transactions" : user.transactions.all().order_by("-created_at"),
    }
    return render(request, 'budget_app/partials/added_tran.html', context)

@csrf_exempt
def update_cards(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "cards": user.cards.all()
    }
    return render(request, 'budget_app/partials/added_cards.html', context)

@csrf_exempt
def update_accounts(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "accounts": user.accounts.all()
    }
    return render(request, 'budget_app/partials/added_accounts.html', context)

@csrf_exempt
def update_tran(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "transactions": user.transactions.all()
    }
    return render(request, 'budget_app/partials/added_tran.html', context)

@csrf_exempt
def payment(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "accounts": user.accounts.all(),
        "cards": user.cards.all()
    }
    return render(request, 'budget_app/partials/payment.html', context)

@csrf_exempt
def purchase(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "accounts": user.accounts.all(),
        "cards": user.cards.all()
    }
    return render(request, 'budget_app/partials/purchase.html', context)

@csrf_exempt
def deposit(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "accounts": user.accounts.all()
    }
    return render(request, 'budget_app/partials/deposit.html', context)

@csrf_exempt
def withdraw(request) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "accounts": user.accounts.all()
    }
    return render(request, 'budget_app/partials/withdraw.html', context)

@csrf_exempt
def edit_card(request, id) :
    user = User.objects.get(id=request.session['userid'])
    context = {
        "card": Card.objects.get(id=id),
        "cards": user.cards.all()
    }
    return render(request, 'budget_app/partials/edit_cards.html', context)

@csrf_exempt
def edit_account(request, id) :
    context = {
        "account": Account.objects.get(id=id)
    }
    return render(request, 'budget_app/partials/edit_accounts.html', context)

@csrf_exempt
def update_card(request) :
    card = Card.objects.get(id=request.POST.get('card_id'))
    errors = Card.objects.EditNameValidator(request.POST, card.name)
    if len(errors) > 0 :
        return render(request, 'budget_app/partials/c_err.html')
    else :
        card.name = request.POST['edit_card_name']
        card.balance = request.POST['edit_card_balance']
        card.save()
        user = User.objects.get(id=request.session['userid'])
        context = {
            "cards": user.cards.all()
        }
        return render(request, 'budget_app/partials/added_cards.html', context)

@csrf_exempt
def update_account(request) :
    account = Account.objects.get(id=request.POST['account_id'])
    errors = Account.objects.EditNameValidator(request.POST, account.name)
    if len(errors) > 0 :
        return render(request, 'budget_app/partials/a_err.html')
    else :
        account.name = request.POST['edit_account_name']
        account.balance = request.POST['edit_account_balance']
        account.save()
        user = User.objects.get(id=request.session['userid'])
        context = {
            "accounts": user.accounts.all()
        }
        return render(request, 'budget_app/partials/added_accounts.html', context)