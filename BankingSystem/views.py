from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Serviceuser, Deposit, Withdraw, SendMoney

# Create your views here.
def index(request):
	return render(request,'BankingSystem/index.html')

def withdraw(request):
	if request.method=="POST":
		name_id=request.POST.get('user')
		name = Serviceuser.objects.get(id=name_id)
		amount = request.POST.get('amount')
		w = Withdraw.objects.create(serviceuser=name,withdraw_amount=amount)
		w.save()
		update = Serviceuser.objects.get(pk=name_id)
		update.balance-=int(amount)
		update.save()
		return render(request,'BankingSystem/withdraw.html',{'msg':'Money Withdrawed Successfully',
			'users':Serviceuser.objects.all()})

	else:
		return render(request,'BankingSystem/withdraw.html',{'users':Serviceuser.objects.all()})

def deposit(request):
	users = Serviceuser.objects.all()
	if request.method=="POST":
		name_id=request.POST.get('user')
		name = Serviceuser.objects.get(id=name_id)
		amount = request.POST.get("amount")
		x=Deposit.objects.create(serviceuser=name,deposit_amount=amount)
		x.save()
		y=Serviceuser.objects.get(pk=name_id)
		#print(type(y.balance))
		print(type(amount))
		y.balance+=int(amount)
		y.save()
		return render(request,'BankingSystem/deposit.html',
			{'users':users,'msg':'Deposit Successfully'})
	else:
		return render(request,'BankingSystem/deposit.html',
			{'users':Serviceuser.objects.all()})
		
def userinfo(request):
	bank_users = Serviceuser.objects.all()
	return render(request,'BankingSystem/userinfo.html',{'bank_users':bank_users})

def sendmoney(request):
	if request.method=="POST":
		name_id=request.POST.get('user')
		name = Serviceuser.objects.get(id=name_id)
		name_id1=request.POST.get('user1')
		name1 = Serviceuser.objects.get(id=name_id)
		amount = request.POST.get('amount')
		w = SendMoney.objects.create(serviceuser=name1,amount=amount)
		w.save()
		update = Serviceuser.objects.get(pk=name_id1)
		update.balance+=int(amount)
		update.save()
		update1 = Serviceuser.objects.get(pk=name_id)
		update1.balance-=int(amount)
		update1.save()
		return render(request,'BankingSystem/sendmoney.html',{'msg':'Money Withdrawed Successfully',
			'users':Serviceuser.objects.all()})

	else:
		return render(request,'BankingSystem/sendmoney.html',{'users':Serviceuser.objects.all()})
	#if request=="POST":
		
		#name_id = request.POST.get('f_user')
		#f_name = Serviceuser.objects.get(id=from_name_id)
		#to_name_id = request.post.get('t_user')
		#t_name = Serviceuser.objects.get(id=to_name_id)
		#amount = request.POST.get('amount')
		#send_money = SendMoney.objects.create(serviceuser=f_name,amount=amount)
		#send_money.save()
		#f = Serviceuser.objects.get(pk=from_name_id)
		#f.balance-=int(amount)
		#f.save()
		#t = Serviceuser.objects.get(pk=to_name_id)
		#t.balance+=int(amount)
		#t.save()

		#return render(request,'BankingSystem/sendmoney.html',{'users':Serviceuser.objects.all(),
		#	'msg':'Money Transfered Successfully!'})
	#else:
		#return render(request,'BankingSystem/sendmoney.html',{'users':Serviceuser.objects.all()})

def home(request,pk):
	users = Serviceuser.objects.filter(pk=pk)
	return render(request,'BankingSystem/home.html',{'users':users})

def adduser(request):
	if request.method=="POST":
		name = request.POST.get('name')
		nid = request.POST.get('nid')
		date = request.POST.get('date')
		balance = request.POST.get('balance')
		user = Serviceuser.objects.create(name=name,nid_no=nid,date_created=date,balance=balance)
		user.save()
		print('YES MAN')
		return render(request,'BankingSystem/adduser.html',{'msg':'Account Created Successfully'})
	else:
		print("LOL ")
		return render(request,'BankingSystem/adduser.html')
		







