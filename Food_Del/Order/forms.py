from django import forms
from .models import Ord_ADD

class ADDForm(forms.ModelForm):
	class Meta:
		model=Ord_ADD
		fields=['Area','City','Pincode','Mnumber']
