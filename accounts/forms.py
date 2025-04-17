from django import forms
from .models import User

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = "__all__"

      def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
      #   self.fields['mail'].widget = forms.TextInput(attrs={'readonly': 'readonly'})