from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

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