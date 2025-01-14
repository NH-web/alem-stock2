from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import Stock, History
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib.auth.models import User
import sqlite3


all_users = User.objects.values()

username_list = []
for i in range(len(all_users)):
	username_list.append(all_users[i]['username'])

# Create your views here.
admins_list = ['banchi','beti','teddy']
def home(request):
	title = "welcome : this is the homepage"
	form = ""
	context = {
	"title":title,
	"form":form,
	}
	if request.user.is_authenticated:
		if str(request.user) in admins_list:
			return redirect('/admin_dashboard')

		else:
			return redirect('/dashboard')
	else:
		return render(request, 'home.html', context)
@login_required
def dashboard(request):
	if str(request.user) in admins_list:
		return redirect('/admin_dashboard')
	else:
		form = StockSearchform(request.POST or None)
		title = 'Dashboard'
		pi = Stock.objects.filter(username__icontains=request.user)
		prev = pi[::-1]
		p = History.objects.filter(history_username__icontains=request.user)
		category_list_name = []
		cat_prices = []
		sales_prices = []
		purch_prices = []
		sales_amount = []
		purch_amount = []
		s_amount = []
		p_amount = []
		timestamps = []
		date_graph = []
		dates = []
		for i in range(len(p)):
			l = p[i].history_category
			category_list_name.append(l)
			pp = p[i].history_sales_price
			oks = p[i].history_purch_quantity
			p_amount.append(oks)
			okp = -1 * p[i].history_sales_quantity
			s_amount.append(okp)
			cat_prices.append(pp)
			datee= p[i].history_last_updated
			timestamps.append(datee)
			

		for i in range(len(pi)):
			okl = pi[i].purch_quantity
			purch_amount.append(okl)
			oks = -1 * pi[i].sales_quantity
			sales_amount.append(oks)
		for i in range(len(timestamps)):
			date_graph.append([timestamps[i].year,timestamps[i].month, timestamps[i].day])
		
		print (dates)
		for l in range(len(prev)):
			p = prev[l].sales_price
			k = p * prev[l].sales_quantity
			sales_prices.append(k)
			c = prev[l].purch_price
			kp = c * prev[l].purch_quantity
			purch_prices.append(kp)

		context = {
		"title":title,
		"quaryset":prev,
		"role":"worker",
		"approved":1,
		"cat_prices":cat_prices,
		"cat_list":category_list_name,
		"sales_price":sum(sales_prices),
		"purch_price":sum(purch_prices),
		"sales_amount":sum(sales_amount),
		"sales_amount_graph":s_amount,
		"purch_amount_graph":p_amount,
		"sales_price_graph":sales_prices,
		"purch_price_graph":purch_prices,
		"date_graph":date_graph,
		"purch_amount":sum(purch_amount),
		"form":form,
		}
		print (sum(sales_amount))
		print (sum(purch_amount))
		if request.method == 'POST':
			quaryset = Stock.objects.filter(category__contains=form['category'].value())
			context = {
			"title":title,
			"quaryset":quaryset,
			"role":"worker",
				"approved":1,
		"cat_prices":cat_prices,
		"cat_list":category_list_name,
		"sales_price":sum(sales_prices),
		"purch_price":sum(purch_prices),
		"sales_amount":sum(sales_amount),
		"sales_amount_graph":s_amount,
		"purch_amount_graph":p_amount,
		"sales_price_graph":sales_prices,
		"purch_price_graph":purch_prices,
		"date_graph":date_graph,
		"purch_amount":sum(purch_amount),
		"form":form,
			}
		return render(request, "dashboard.html", context)
@login_required
def admin_dashboard(request):
	if str(request.user) in admins_list:
		form = StockSearchform(request.POST or None)
		title = 'Dashboard'
		pi = Stock.objects.all()
		prev = pi[::-1]
		p = History.objects.all()
		category_list_name = []
		cat_prices = []
		sales_prices = []
		purch_prices = []
		sales_amount = []
		purch_amount = []
		timestamps = []
		date_graph = []
		dates = []
		for i in range(len(p)):
			okl = p[i].history_purch_quantity
			purch_amount.append(okl)
			oks = -1 * p[i].history_sales_quantity
			sales_amount.append(oks)
			datee= p[i].history_last_updated
			timestamps.append(datee)
		for i in range(len(timestamps)):
			date_graph.append([timestamps[i].month, timestamps[i].day])
		
		for l in range(len(prev)):
			o = prev[l].category
			category_list_name.append(o)
			s = prev[l].sales_price
			cat_prices.append(s)
			p = prev[l].sales_price
			k = p * prev[l].sales_quantity
			sales_prices.append(k)
			c = prev[l].purch_price
			kp = c * prev[l].purch_price
			purch_prices.append(kp)
		print (dates)
		context = {
		"title":title,
		"quaryset":prev,
		"role":"Manager",
		"approved":1,
		"cat_prices":cat_prices,
		"cat_list":category_list_name,
		"sales_price":sum(sales_prices),
		"purch_price":sum(purch_prices),
		"sales_amount":sum(sales_amount),
		"sales_amount_graph":sales_amount,
		"purch_amount_graph":purch_amount,
		"sales_price_graph":sales_prices,
		"purch_price_graph":purch_prices,
		"date_graph":date_graph,
		"purch_amount":sum(purch_amount),
		"form":form,
		}
		if request.method == 'POST':
			quaryset = Stock.objects.filter(username__icontains=form['username'].value())
			pp = History.objects.filter(history_username__icontains=form['username'].value())
			salesamount = []
			purchamount = []

			context = {
		    "title":title,
		    "quaryset":quaryset,
		    "role":"Manager",
		    "approved":1,
		    "cat_prices":cat_prices,
	    	"cat_list":category_list_name,
		    "sales_price":sum(sales_prices),
		    "purch_price":sum(purch_prices),
		    "sales_amount":sum(sales_amount),
		    "sales_amount_graph":sales_amount,
    		"purch_amount_graph":purch_amount,
    		"sales_price_graph":sales_prices,
		    "purch_price_graph":purch_prices,
		    "date_graph":date_graph,
		    "purch_amount":sum(purch_amount),
		    "form":form,
		    }
		return render(request, "dashboard.html", context)
	else:
		return redirect('/dashboard')
@login_required
def stock_list(request):
	if str(request.user) in admins_list:
		return redirect('/stock_list_all')
	else:
		form = StockSearchform(request.POST or None)
		title = f'{request.user} Stock'
		p = Stock.objects.filter(username__icontains=request.user)
		purch_amount = []
		sales_amount = []
		beg_amount = []
		for i in range(len(p)):
			purch_amount.append(p[i].purch_quantity)
			sales_amount.append(p[i].sales_quantity)
			beg_amount.append(p[i].beg_quantity)
		if len(sales_amount) != 0:
			sales_total = sum(sales_amount)
			purch_total = sum(purch_amount)
			total = sum(beg_amount) + purch_total
			sales_percent = sales_total/total * 100
			purch_percent = purch_total/total * 100
			context = {
				"title":title,
				"quaryset":p,
				"role":"Worker",
				"sales_percent":round(sales_percent,2),
				"purch_percent":round(purch_percent,2),
				"sales_amount":sum(sales_amount),
				"purch_amount":sum(purch_amount),
				"form":form,
				}
		else:
			context = {
				"title":title,
				"quaryset":p,
				"role":"Worker",
				"form":form,
				}
		
		if request.method == 'POST':
			quaryset = Stock.objects.filter(username__icontains=request.user)
			if form['export_to_csv'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = 'attachment; filename="List_of_stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','BEG_QTY','SALES_QTY','PURCH_QUANTITY' ,'QUANTITY ON HAND', 'TIMESTAMP'])
				instance = quaryset
				for stock in instance:
					writer.writerow([stock.category, stock.username, stock.beg_quantity, stock.sales_quantity, stock.purch_quantity, stock.onhand,stock.timestamp])
				return response
			context = {
			"form":form,
			"title":title,
			"role":"Worker",
			"sales_percent":round(sales_percent,2),
			"purch_percent":round(purch_percent,2),
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"quaryset":quaryset
			}
		return render(request, "stocklist.html", context)
@login_required
def stock_list_all(request):
	if str(request.user) in admins_list:
		form = StockSearchform(request.POST or None)
		title = f'{request.user} Stock'
		p = Stock.objects.all()
		purch_amount = []
		sales_amount = []
		beg_amount = []
		
		for i in range(len(p)):
			purch_amount.append(p[i].purch_quantity)
			sales_amount.append(p[i].sales_quantity)
			beg_amount.append(p[i].beg_quantity)
		if len(sales_amount) != 0:
			sales_total = sum(sales_amount) 
			purch_total = sum(purch_amount)
			total = sum(beg_amount) + purch_total
			sales_percent = sales_total/total * 100
			purch_percent = purch_total/total * 100
			context = {
				"title":title,
				"quaryset":p,
				"role":"Manager",
				"username_list":username_list,
				"sales_percent":round(sales_percent,2),
				"purch_percent":round(purch_percent,2),
				"sales_amount":sum(sales_amount),
				"purch_amount":sum(purch_amount),
				"form":form,
				}
		else:
			context = {
				"title":title,
				"quaryset":p,
				"username_list":username_list,
				"sales_amount":sum(sales_amount),
				"purch_amount":sum(purch_amount),
				"role":"Manager",
				"form":form,
				}
	
		if request.method == 'POST':
			quaryset = Stock.objects.filter(username__icontains=form['username'].value())
			if form['export_to_csv'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = 'attachment; filename="List_of_stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','BEG_QTY','SALES_QTY','PURCH_QUANTITY' ,'QUANTITY ON HAND', 'TIMESTAMP'])
				instance = quaryset
				for stock in instance:
					writer.writerow([stock.category, stock.username, stock.beg_quantity, stock.sales_quantity, stock.purch_quantity, stock.onhand,stock.timestamp])
				return response
			context = {
			"form":form,
			"title":title,
			"role":"Manager",
			"username_list":username_list,
			"sales_percent": round(sales_percent, 2),
			"purch_percent":round(purch_percent,2),
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"quaryset":quaryset
			}
		return render(request, "stocklistadmin.html", context)
	else:
		return redirect('/stock_list')
@login_required
def stock_list_user(request, pk):
	if str(request.user) in admins_list:
		form = StockSearchform(request.POST or None)
		title = f'{request.user} Stock'
		p = Stock.objects.filter(username__icontains=pk)
		purch_amount = []
		sales_amount = []
		beg_amount = []
		
		for i in range(len(p)):
			purch_amount.append(p[i].purch_quantity)
			sales_amount.append(p[i].sales_quantity)
			beg_amount.append(p[i].beg_quantity)
		if len(sales_amount) != 0:
			sales_total = sum(sales_amount)
			purch_total = sum(purch_amount) 
			total = sum(beg_amount) + purch_total
			sales_percent = sales_total/total * 100
			purch_percent = purch_total/total * 100
			context = {
				"title":title,
				"quaryset":p,
				"role":"Manager",
				"sales_percent":round(sales_percent,2),
				"purch_percent":round(purch_percent,2),
				"sales_amount":sum(sales_amount),
				"purch_amount":sum(purch_amount),
				"username_list":username_list,
				"form":form,
				}
		else:
			context = {
				"title":title,
				"quaryset":p,
				"role":"Manager",
				"sales_amount":sum(sales_amount),
				"purch_amount":sum(purch_amount),
				"username_list":username_list,
				"form":form,
				}
		if request.method == 'POST':
			quaryset = Stock.objects.filter(username__icontains=request.user)
			if form['export_to_csv'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = 'attachment; filename="List_of_stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','BEG_QTY','SALES_QTY','PURCH_QUANTITY' ,'QUANTITY ON HAND', 'TIMESTAMP'])
				instance = quaryset
				for stock in instance:
					writer.writerow([stock.category, stock.username, stock.beg_quantity, stock.sales_quantity, stock.purch_quantity, stock.onhand,stock.timestamp])
				return response
			context = {
			"form":form,
			"title":title,
			"role":"Manager",
			"username_list":username_list,
			"sales_percent":round(sales_percent,2),
			"purch_percent":round(purch_percent,2),
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"quaryset":quaryset
			}
		return render(request, "stocklistadmin.html", context)
	else:
		return redirect('/stock_list')

@login_required
def add_items(request):
	form = StockCreateform(request.POST or None)
	o = Stock.objects.filter(username__icontains=request.user)
	if str(request.user) in admins_list:
		role = "Manager"
	else:
		role = "Worker"
	if form.is_valid():
		form.save(commit=False)
		if form['username'].value() == str(request.user):
			form.save()
			messages.success(request, 'Successfully Added')
			if str(request.user) in admins_list:
				return redirect('/stock_list_all')
			else:
				return redirect('/stock_list')
		else:
			messages.success(request, "Username doesn't much your login")
			return redirect('/add_items')
	context = {
	"form":form,
	"title":"Add Items",
	"quaryset":o,
	"role":role,
	}
	return render(request,"new_add_item.html", context)

@login_required
def update_items(request, pk):
	quaryset = Stock.objects.get(id=pk)
	form = StockUpdateform(instance=quaryset)
	if request.method == 'POST':
		form = StockUpdateform(request.POST, instance=quaryset)

		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Updated')

			if str(request.user) in admins_list:
				return redirect('/stock_list_all')
			else:
				return redirect('/stock_list')
	context = {
	'form':form
	}
	return render(request, 'update_items.html', context)

def delete_items(request, pk):
	quaryset = Stock.objects.get(id=pk)
	if request.method == "POST":
		quaryset.delete()
		messages.success(request, 'Successfully Deleted')
		if str(request.user) in admins_list:
			return redirect('/stock_list_all')
		else:
			return redirect('/stock_list')
	return render(request, 'delete_items.html')
@login_required
def stock_detail(request, pk):
		if str(request.user) in admins_list:
			role = "Manager"
		else:
			role = "Worker"
		quaryset = Stock.objects.get(id=pk)
		form = HistorySearchform(request.POST or None)
		k = str(quaryset.category)
		p = History.objects.filter(history_category__icontains=k,history_username__icontains=quaryset.username)
		preverse = p[::-1]
		
		category_list_name = quaryset.category
		cat_prices = quaryset.sales_price
		sales_prices = []
		purch_prices = []
		sales_amount = []
		purch_amount = []
		
		for i in range(len(p)):
			pp = p[i].history_sales_price
			onh = -pp * p[i].history_issue_quantity
			sales_prices.append(onh)
			ons = p[i].history_purch_price * p[i].history_receive_quantity
			purch_prices.append(ons)
			okl = p[i].history_receive_quantity
			purch_amount.append(okl)
			oks = p[i].history_issue_quantity 
			sales_amount.append(oks)
		context = {
		"title":quaryset.category,
		"quaryset":quaryset,
		"p":preverse,
		"role":role,
		"cat_prices":cat_prices,
		"cat_list":category_list_name,
		"sales_price":sum(sales_prices),
		"purch_price":sum(purch_prices),
		"sales_amount":sum(sales_amount),
		"purch_amount":sum(purch_amount),
		"form":form,
		}
		if request.method == 'POST':
			quar = History.objects.filter(history_fs_number__icontains=form['history_fs_number'].value(), history_targa_number__icontains=form['history_targa_number'].value())
           
			context = {
			"form":form,
			"quaryset":quaryset,
			"cat_prices":cat_prices,
			"cat_list":category_list_name,
			"sales_price":sum(sales_prices),
			"purch_price":sum(purch_prices),
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"role":role,
			"p":quar,
			}
		return render(request, "new_stock_detail.html", context)


def issue_items(request, pk):
	quaryset =Stock.objects.get(id=pk)
	form = Issueform(request.POST or None, instance=quaryset)
	if str(request.user) in admins_list:
		role = "Manager"
	else:
		role = "Worker"
	if form.is_valid():
		instance = form.save(commit=False)
		if form['username'].value() == str(request.user):
			if instance.issue_quantity <= instance.onhand:
				instance.sales_quantity -= instance.issue_quantity
				instance.onhand -= instance.issue_quantity
				price = instance.issue_quantity * instance.sales_price
				instance.notification = f"({str(instance.last_updated.year)}/{str(instance.last_updated.month)}/{str(instance.last_updated.day)} - {str(instance.last_updated.hour)}:{str(instance.last_updated.minute)})  {request.user} Issued {str(instance.issue_quantity)} pieces of '{str(instance.category)}' For the FS NUMBER '{str(instance.fs_number)}' for a Total price of {str(price)}"
				messages.success(request, "Issued Successfully. " + str(instance.onhand) + " " + str(instance.category) + "s now left in Store")
				instance.save()
				return redirect(f"/add_to_history/{str(instance.category)}/{str(instance.username)}/{int(instance.issue_quantity)}/0/{int(instance.fs_number)}/none/{int(instance.purch_quantity)}/{str(instance.sales_quantity)}/{str(instance.sales_price)}/{str(instance.purch_price)}/{int(instance.onhand)}")

			else:
				messages.success(request, "Sorry But you don't have enough amount on hand")
		else:
			messages.success(request, "Sorry but username doesn't match")
	context = {
	"title":'ISSUE ' ,
	"cat":str(quaryset.category),
	"role":role,
	"quaryset":quaryset,
	"form":form,
	}
	return render(request, "issue_item.html",context)
@login_required
def notification(request):
	if str(request.user) in admins_list:
		quaryset = Stock.objects.all()
		lastupdatd = []
		lastupdated = []
		for i in range(len(quaryset)):
			lastupdatd.append(quaryset[i].notification)
		for l in lastupdatd:
			if l == "" or l == None:
				l = "No Notification Yet"
			else:
				l = l
			lastupdated.append(l)
		context = {
		"title":"Notification ",
		"role":"Manager",
		"quaryset":quaryset,
		"date":sorted(lastupdated)
		}
		
		return render(request, "notification.html", context)
	else:
		quaryset = Stock.objects.filter(username__icontains=request.user)
		lastupdatd = []
		lastupdated= []
		for i in range(len(quaryset)):
			lastupdatd.append(quaryset[i].notification)
		for l in lastupdatd:
			if l == "" or l == None:
				l = "No Notification Yet"
			else:
				l = l
			lastupdated.append(l)
		context = {
		"title":f"Notification ",
		"role":"Worker",
		"quaryset":quaryset,
		"date":sorted(lastupdated)
		}
		return render(request, "notification.html", context)
def receive_items(request, pk):
	quaryset =Stock.objects.get(id=pk)

	form = Receiveform(request.POST or None, instance=quaryset)
	if str(request.user) in admins_list:
		role = "Manager"
	else:
		role = "Worker"
	if form.is_valid():
		if form['username'].value() == str(request.user):
			instance = form.save(commit=False)
			instance.purch_quantity += instance.receive_quantity
			instance.onhand += instance.receive_quantity
			price = instance.receive_quantity * instance.purch_price
			instance.notification = f"({str(instance.last_updated.year)}/{str(instance.last_updated.month)}/{str(instance.last_updated.day)} - {str(instance.last_updated.hour)}:{str(instance.last_updated.minute)})   {request.user} Received {str(instance.receive_quantity)} pieces of '{str(instance.category)}' from Targa Number '{str(instance.targa_number)}' for a Total price of {str(price)}"
			instance.save()

			messages.success(request, "Received Successfully. " + str(instance.onhand) + " " + str(instance.category) + "s now in Store")
			return redirect(f"/add_to_history/{str(instance.category)}/{str(instance.username)}/0/{int(instance.receive_quantity)}/0/{str(instance.targa_number)}/{int(instance.purch_quantity)}/{str(instance.sales_quantity)}/{str(instance.sales_price)}/{str(instance.purch_price)}/{int(instance.onhand)}")
			#return redirect(f"/add_to_history/{str(instance.category)}/{str(request.user)}/{0}/{int(instance.receive_quantity)}/{0}/{str(instance.targa_number)}/{int(instance.purch_quantity)}/{str(instance.sales_quantity)}/{str(instance.sales_price)}/{str(instance.purch_price)}/")
		else:
			messages.success(request, "Sorry But Username not correct")
	context = {
	"title":'RECEIVE ',
	"role": role,
	'cat':str(quaryset.category),
	"instance": quaryset,
	"form":form,
	}
	return render(request, "receive_item.html",context)

def add_to_history(request, cat, usern, iss,rec,fs,targa,purch_quan, sales_quan,sales_price, purch_price, onhand):
	History.objects.all()
	his = History(history_category=cat, history_username=usern, history_receive_quantity=rec, history_issue_quantity=iss,history_fs_number=fs, history_targa_number=targa, history_purch_quantity=purch_quan, history_sales_quantity=int(sales_quan), history_sales_price=float(sales_price), history_purch_price=float(purch_price), history_onhand=onhand)
	his.save()
	#History.save()
	return redirect('/')


@login_required
def history_list_all(request):
	if str(request.user) in admins_list:
		form = HistorySearchform(request.POST or None)
		title = f'{request.user}'
		p = History.objects.all()
		userslist = []
		for i in range(len(all_users)):
			userslist.append(all_users[i]['username'])
		context = {
		"title":title,
		"userslist":userslist,
		"quaryset":p,
		"form":form,
		}
		if request.method == 'POST':
			quaryset = History.objects.filter(history_category__icontains=form['history_category'].value())
			if form['export_to_csv'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = f'attachment; filename="{request.user}-stock-history.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','ISSUED','RECEIVED','FS NUMBER' ,'TARGA NUMBER', 'LAST UPDATED'])
				instance = quaryset
				for h in instance:
					writer.writerow([h.history_category, h.history_username, h.history_issue_quantity, h.history_receive_quantity, h.history_fs_number, h.history_targa_number,h.history_last_updated])
				return response
			context = {
			"form":form,
			"title":title,
			"quaryset":quaryset
			}
		return render(request, "historyadmin.html", context)
	else:
		return redirect('/history')
@login_required
def history_list(request):
	if str(request.user) not in admins_list:

		form = HistorySearchform(request.POST or None)
		title = f'{request.user}'
		p = History.objects.filter(history_username__icontains=request.user)
		context = {
		"title":title,
		"quaryset":p,
		"form":form,
		}
		if request.method == 'POST':
			quaryset = History.objects.filter(history_category__icontains=form['history_category'].value(), history_username__icontains=request.user)
			if form['export_to_csv'].value() == True:
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = f'attachment; filename="{request.user}-stock-history.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','ISSUED','RECEIVED','FS NUMBER' ,'TARGA NUMBER', 'LAST UPDATED'])
				instance = quaryset
				for h in instance:
					writer.writerow([h.history_category, h.history_username, h.history_issue_quantity, h.history_receive_quantity, h.history_fs_number, h.history_targa_number,h.history_last_updated])
				return response
			context = {
			"form":form,
			"title":title,
			"quaryset":quaryset
			}
		return render(request, "history.html", context)
	else:
		return redirect('/history_list_all')
	
@login_required
def profile(request):
	if str(request.user) in admins_list:
		quaryset = Stock.objects.all()
		q2 = Stock.objects.filter(username__icontains=request.user)
		form = Reportform(request.POST or None)
		h = History.objects.all()
		sales_amount = []
		purch_amount = []
		beg_amount = []
		for i in range(len(q2)):
			sales_amount.append(-1 * q2[i].sales_quantity)
			purch_amount.append(q2[i].purch_quantity)
			beg_amount.append(q2[i].beg_quantity)
		totalamount = sum(beg_amount) + sum(purch_amount)
		if totalamount == 0:
			sales_ratio = 0
		else:
			sales_ratio = sum(sales_amount)/totalamount
		context ={
		"form":form,
		"quaryset":quaryset,
		"username_list":username_list,
		"role":"Manager",
		"sales_amount":sum(sales_amount),
		"purch_amount":sum(purch_amount),
		"history":h,
		"sales_ratio":sales_ratio,
		}
		if request.method == 'POST':
			dates = []
			if form['export_to_csv'].value() == True:
				stock_quaryset = Stock.objects.filter(username__icontains=form['history_username'].value())
				for i in range(len(stock_quaryset)):
					dates.append(stock_quaryset[i].timestamp)
				f_date = [0]
				l_date = [-1]
				date_range = f"{str(f_date)}-{str(l_date)}"
				ruser = form['history_username'].value()
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = f'attachment; filename="summery_{ruser}_{date_range}_stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','BEG_QTY','SALES_QTY','PURCH_QUANTITY' ,'ON HAND', 'TIMESTAMP'])
				instance = stock_quaryset
				

				for stock in instance:
					writer.writerow([stock.category, stock.username, stock.beg_quantity, stock.sales_quantity, stock.purch_quantity, stock.onhand,stock.timestamp])
				return response
			elif form['history_export_to_csv'].value() == True:
				history_quaryset = History.objects.filter(history_category__icontains=form['history_category'].value(),history_username__icontains=form['history_username'].value())
				hdates = []
				for i in range(len(history_quaryset)):
					hdates.append(history_quaryset[i].history_last_updated)
				hf_date = [0]
				hl_date = [-1]
				hdate_range = f"{str(hf_date)}-{str(hl_date)}"
				ruser = form['history_username'].value()
				history_response = HttpResponse(content_type='text/csv')
				history_response['Content.Disposition'] = f'attachment; filename="history_{ruser}_{hdate_range}_stock.csv"'
				hwriter = csv.writer(history_response)
				hwriter.writerow(['CATEGORY','USERNAME','SALES QUANTITY','FS NUMBER','SALES PRICE','PURCHASE QUANTITY','TARGA NUMBER','PURCHASE PRICE','LAST UPDATED'])				
				hinstance = history_quaryset
				for history in hinstance:
					hwriter.writerow([history.history_category, history.history_username,history.history_sales_quantity,history.history_fs_number,history.history_sales_price,history.history_purch_quantity,history.history_targa_number,history.history_purch_price,history.history_last_updated])
				return history_response
			context ={
			"form":form,
			"quaryset":quaryset,
			"username_list":username_list,
			"role":"Manager",
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"history":h,
			"sales_ratio":sales_ratio,
			}
		return render(request, 'profile.html',context)
	else:
		quaryset = Stock.objects.filter(username__icontains=request.user)
		form = Reportform(request.POST or None)
		h = History.objects.filter(history_username__icontains=request.user)
		sales_amount = []
		purch_amount = []
		beg_amount = []

		for i in range(len(quaryset)):
			sales_amount.append(-1 * quaryset[i].sales_quantity)
			purch_amount.append(quaryset[i].purch_quantity)
			beg_amount.append(quaryset[i].beg_quantity)
		totalamount = sum(beg_amount) + sum(purch_amount)
		if totalamount == 0:
			sales_ratio = 0
		else:
			sales_ratio = sum(sales_amount)/totalamount

		context ={
		"form":form,
		"quaryset":quaryset,
		"role":"worker",
		"sales_amount":sum(sales_amount),
		"purch_amount":sum(purch_amount),
		"history":h,
		"sales_ratio":sales_ratio
		}
		ruser = str(request.user)
		if request.method == 'POST':
			if form['export_to_csv'].value() == True:
				stock_quaryset = Stock.objects.filter(username__icontains=request.user)
				dates = []
				ruser = str(request.user)
				for i in range(len(stock_quaryset)):
					dates.append(stock_quaryset[i].timestamp)
				f_date = [0]
				l_date = [-1]
				date_range = f"{str(f_date)}-{str(l_date)}"
				response = HttpResponse(content_type='text/csv')
				response['Content.Disposition'] = f'attachment; filename="summery_{ruser}_{date_range}_stock.csv"'
				writer = csv.writer(response)
				writer.writerow(['CATEGORY', 'USERNAME','BEG_QTY','SALES_QTY','PURCH_QUANTITY' ,'ON HAND', 'TIMESTAMP'])
				instance = stock_quaryset
				

				for stock in instance:
					writer.writerow([stock.category, stock.username, stock.beg_quantity, stock.sales_quantity, stock.purch_quantity, stock.onhand,stock.timestamp])
				return response
			elif form['history_export_to_csv'].value() == True:
				history_quaryset = History.objects.filter(history_category__icontains=form['history_category'].value(), history_username__icontains=request.user)
				hdates = []
				for i in range(len(history_quaryset)):
					hdates.append(history_quaryset[i].history_last_updated)
				hf_date = [0]
				hl_date = [-1]
				hdate_range = f"{str(hf_date)}-{str(hl_date)}"
				history_response = HttpResponse(content_type='text/csv')
				history_response['Content.Disposition'] = f'attachment; filename="history_{ruser}_{hdate_range}_stock.csv"'
				hwriter = csv.writer(history_response)
				hwriter.writerow(['CATEGORY','USERNAME','SALES QUANTITY','FS NUMBER','SALES PRICE','PURCHASE QUANTITY','TARGA NUMBER','PURCHASE PRICE','LAST UPDATED'])				
				hinstance = history_quaryset
				for history in hinstance:
					hwriter.writerow([history.history_category, history.history_username,history.history_sales_quantity,history.history_fs_number,history.history_sales_price,history.history_purch_quantity,history.history_targa_number,history.history_purch_price,history.history_last_updated])
				return history_response
			context ={
			"form":form,
			"quaryset":quaryset,
			"role":"Worker",
			"sales_amount":sum(sales_amount),
			"purch_amount":sum(purch_amount),
			"history":h,
			"sales_ratio":sales_ratio,
			}
		return render(request, 'profile.html',context)


	


	
