from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import *

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request, 'pages/index.html',{
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    })

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    return render(request, 'pages/about.html',{
        'realtors': realtors
    })