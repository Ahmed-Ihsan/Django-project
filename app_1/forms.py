from django import forms

class input_post(forms.Form):
	title = forms.CharField(required=True )
	text = forms.CharField(required=True )
	img = forms.ImageField(required=True )
	many = forms.IntegerField(required=True )

class input_user(forms.Form):
	first_name=forms.CharField(required=True)
	lest_name=forms.CharField(required=True)
	age=forms.IntegerField(required=True)
	date_bith=forms.DateTimeField(required=True)
