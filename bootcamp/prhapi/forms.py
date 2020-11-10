from django import forms

class CompanyForm(forms.Form):
    business_id = forms.CharField(label='Company business ID', max_length=10)