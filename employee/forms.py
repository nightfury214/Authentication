from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
   class Meta:
      model = Employee
      fields = "__all__"

      def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['mail'].widget = forms.TextInput(attrs={'readonly': 'readonly'})