from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from listings.choices import *

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request,'listings/listings.html',{
        'listings': paged_listings
    })

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    return render(request, 'listings/listing.html',{
        'listing': listing
    })

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)

        # State
        if 'state' in request.GET:
            state = request.GET['state']
            if state:
                queryset_list = queryset_list.filter(state__iexact=state)
    
    paginator = Paginator(queryset_list,6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    return render(request, 'listings/search.html',{
        'listings': paged_listing,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    })
