from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Device
from django.contrib.auth.models import User
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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmer le mot de passe"

        # Remove default help text
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

# Customize login form to replace django default labels
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['password'].label = "Mot de passe"

