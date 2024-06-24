from django import forms
from .models import Device, GDPR
from django.contrib.auth.forms import UserCreationForm

class AddDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'value', 'units', 'deviceStatus']
        widgets = {
            'deviceStatus': forms.Select(attrs={'class': 'help-msg'}),
        }

    # Check if device name already exists
    def clean_device_name(self):
        device_name = self.cleaned_data['name']
        if Device.objects.filter(device_name=device_name).exists():
            raise forms.ValidationError("Device with this name already exists.")
        return device_name
    

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = GDPR
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        # Remove default help text
        def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None  # Remove default help text
