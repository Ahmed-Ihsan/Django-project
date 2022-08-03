from django.forms import ModelForm
from .models import item ,sales

class itemForm(ModelForm):
    class Meta:
        model = item
        fields = '__all__'

class salesForm(ModelForm):
    class Meta:
        model = sales
        fields = '__all__'