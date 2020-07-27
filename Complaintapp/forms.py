from django import forms
from Complaintapp.models import ComplaintInfo

class InfoForm(forms.ModelForm):
    class Meta():
        model=ComplaintInfo
        fields="__all__"