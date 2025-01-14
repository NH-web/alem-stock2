from django import forms
from .models import Stock, History

class StockCreateform(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','beg_quantity','sales_price','username','onhand']

	def clean_category(self):
		category = self.cleaned_data.get('category')
		if not category:
			raise forms.ValidationError('This field is required')
			for i in Stock.objects.all():
				if i.category == category:
						raise forms.ValidationError(item_name + ' is already created')
		return category
	def clean_quantity(self):
		beg_quantity = self.cleaned_data.get('beg_quantity')
		if not beg_quantity:
			raise forms.ValidationError('This field is required')

		return beg_quantity



class Register(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['stockname']
		
class StockSearchform(forms.ModelForm):
	export_to_csv = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ['username']
class HistorySearchform(forms.ModelForm):
	export_to_csv = forms.BooleanField(required=False)
	class Meta:
		model = History
		fields = ['history_category','history_fs_number','history_targa_number']
			
class StockUserform(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['username']
class StockListform(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category']
		
class StockUpdateform(forms.ModelForm):
	class Meta(object):
		model = Stock
		fields = ['category']

class Issueform(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','username','issue_quantity','fs_number']

class Receiveform(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category','username','receive_quantity','targa_number','purch_price']
class Reportform(forms.ModelForm):
	export_to_csv = forms.BooleanField(required=False)
	history_export_to_csv = forms.BooleanField(required=False)
	class Meta:
		model = History
		fields = ['history_category','history_username']


