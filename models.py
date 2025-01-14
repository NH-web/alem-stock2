from django.db import models

# Create your models here.



category_list = (
	('OAK VENEER MDF D. F 18MM','OAK VENEER MDF D. F 18MM'),
	('OAK MDF 5.7MM','OAK MDF 5.7MM'),
	('OAK MDF 12MM','OAK MDF 12MM'),
	('RAW MDF 18MM','RAW MDF 18MM'),
	('RAW MDF 5.7MM','RAW MDF 5.7MM'),
	('MELAMINE MDF S.F 2.6MM','MELAMINE MDF S.F 2.6MM'),
	('LAMINATE MDF 18MM','LAMINATE MDF 18 MM'),
	('CHIPWOOD','CHIPWOOD'),
	('DOOR SKIN DC-92','DOOR SKIN DC-92'),
	('18MM PLASTIC FILM FACED P.D','18MM PLASTIC FILM FACED P.D'),
	('KICHEN TOP 18MM','KICHEN TOP 18MM'),
	('KICHEN TOP 25MM','KICHEN TOP 25MM'),
	('CHIPWOOD LAMINATED','CHIPWOOD LAMINATED'),
	('LAMINATED PLYWOOD 18MM','LAMINATED PLYWOOD 18MM'),
	('A.UV-BOARD','A.UV-BOARD'),
	('ROW 12MM','ROW 12MM'),
	('ROW 2.6MM','ROW 2.6MM'),
	('HARDBOARD 1.8MM','HARDBOARD 1.8MM'),
	('LAMINATE MDF 5.7MM','LAMINATE MDF 5.7MM')
	)


class Category(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name






class Stock(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
	stockname = models.CharField(max_length=200, blank=False, null=False)
	username = models.CharField(max_length=100 ,blank=False,null=False)
	beg_quantity = models.IntegerField(default=0, blank=False, null=False)
	purch_quantity = models.IntegerField(default=0, blank=True, null=True)
	sales_quantity = models.IntegerField(default=0, blank=True, null=True)
	onhand = models.IntegerField(default=0, blank=False, null=False)
	notification = models.CharField(max_length=300, blank=True, null=True)
	fs_number = models.IntegerField(default=0, blank=False, null=False)
	targa_number = models.CharField(max_length=50, blank=False, null=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	issue_quantity = models.IntegerField(default=0, blank=True, null=True)
	receive_quantity = models.IntegerField(default=0, blank=True, null=True)
	issue_to = models.CharField(max_length=200, blank=True, null=True)
	sales_price = models.FloatField(default=0,blank=False,null=False)
	purch_price = models.FloatField(default=0,blank=False,null=False)

class History(models.Model):
	history_category = models.CharField(max_length=100 ,blank=True,null=True)	
	history_stockname = models.CharField(max_length=200, blank=False, null=False)
	history_username = models.CharField(max_length=100 ,blank=False,null=False)
	history_fs_number = models.IntegerField(default=0, blank=True, null=True)
	history_purch_quantity = models.IntegerField(default=0, blank=True, null=True)
	history_sales_quantity = models.IntegerField(default=0, blank=True, null=True)
	history_targa_number = models.CharField(max_length=50, blank=True, null=True)
	history_last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	history_issue_quantity = models.IntegerField(default=0, blank=True, null=True)
	history_receive_quantity = models.IntegerField(default=0, blank=True, null=True)
	history_sales_price = models.FloatField(default=0, blank=False, null=False)
	history_purch_price = models.FloatField(default=0, blank=False, null=False)
	history_onhand = models.IntegerField(default=0, blank=True,null=True)