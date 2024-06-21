from django import forms
from .models import Device

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