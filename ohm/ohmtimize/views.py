import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
from .forms import AddDeviceForm


def index(request):
    '''View function for home page of site.'''

    # Generate counts of some of the main objects
    num_installations = Installation.objects.all().count()
    num_clients = Client.objects.all().count()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_installations': num_installations,
        'num_clients': num_clients,
        'num_visits': num_visits,
    }

    #return HttpResponse("Hello, world. You're at the ohmitimize app index.")
    return render(request, 'index.html', context)

class ClientsListView(generic.ListView):
    model = Client
    paginate_by = 2
    # filter a subset of results to show:
    context_object_name = 'client_list'
    #queryset = Client.objects.filter(memberType='ST')[:5] # Get 5 clients with standard membership
    queryset = Client.objects.all()

class ClientDetailView(generic.DetailView):
    model = Client

class InstallationListView(generic.ListView):
    model = Installation
    paginate_by = 5
    context_object_name = 'installation_list'
    queryset = Installation.objects.all()

class InstallationDetailView(generic.DetailView):
    model = Installation

class ConsumptionByUserListView(LoginRequiredMixin, generic.ListView):
    model = Consumption
    template_name = 'ohmtimize/consumption_by_user.html'

    def get_queryset(self):
        return Consumption.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['production_list'] = Production.objects.filter(user=self.request.user)
        context['grid_exchange_list'] = GridExchange.objects.filter(user=self.request.user)
        return context
    
class DevicesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Device
    template_name = 'ohmtimize/device_list.html'

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['device_list'] = Device.objects.filter(user=self.request.user)
        if self.request.method == 'POST':
            context['form'] = AddDeviceForm(self.request.POST)
        else:
            context['form'] = AddDeviceForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.user = request.user
            new_device.save()
            messages.success(request, 'Device added successfully!', extra_tags='success')
            return redirect('mydevices') 
        return self.get(request, *args, **kwargs)


