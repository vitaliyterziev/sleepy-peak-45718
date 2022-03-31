from django.forms import EmailInput, ModelForm
from .models import Membership


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['email_address']
        widgets = {
            'email_address': EmailInput(attrs={'class': 'col-form-label col-md-4 col-sm-12 pt-0'}),
        }
