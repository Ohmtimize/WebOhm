from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import *

def index(request):
    '''View function for home page of site.'''

    # Generate counts of some of the main objects
    num_installations = Installation.objects.all().count()
    num_clients = Client.objects.all().count()

    context = {
        'num_installations': num_installations,
        'num_clients': num_clients,
    }

    #return HttpResponse("Hello, world. You're at the ohmitimize app index.")
    return render(request, 'index.html', context)

class ClientsListView(generic.ListView):
    model = Client
    # filter a subset of results to show:
    context_object_name = 'client_list'
    queryset = Client.objects.filter(memberType='ST')[:5] # Get 5 clients with standard membership

class ClientDetailView(generic.DetailView):
    model = Client