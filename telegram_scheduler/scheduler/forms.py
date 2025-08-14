from django import forms
from .models import ScheduledMessage

class ScheduledMessageForm(forms.ModelForm):
    class Meta:
        model = ScheduledMessage
        fields = ['message', 'image', 'send_time', 'channels']
        widgets = {
            'channels': forms.CheckboxSelectMultiple(choices=[('USD', 'USD'), ('EUR', 'EUR')]),
        }
