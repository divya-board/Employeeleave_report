
from django import forms
from .models import *



class EmpForm(forms.ModelForm):  #project model form
  class Meta:
    model = Emp
    fields=['id','name','designation','date']

class EmpLeave(forms.ModelForm):
  leave_type = forms.ChoiceField(choices=(("full day", "Full Day"), ("half day", "Half Day")))
  leave_session = forms.ChoiceField(choices=(("", "None"), ("first half", "First Half"), ("second half", "Second Half")))
  class Meta:
    model = Empleav
    fields=['emp_id','emp_name','leave_date_from','leave_date_to','leave_reason','leave_type','leave_session','Status',]

class EmpPermissionForm(forms.ModelForm):
  class Meta:
    model = Empper
    fields=['permission_date','permissionTime_from','permissionTime_To','reason','Status',]
    
