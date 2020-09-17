from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an enquiry already!
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'Already submitted an enquiry!')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(listing=listing, listing_id=listing_id,name=name,phone=phone,email=email,message=message,user_id=user_id)
        contact.save()

        send_mail(
            'Interested in Property',
            f'A user, {name} is interested in property: {listing}',
            'divanshuagarwal2001@gmail.com',
            ['deepikaag75@gmail.com',realtor_email],
            fail_silently=False
        )

        messages.success(request,'Your enquiry has been submitted!')
        return redirect('/listings/'+listing_id)
    else:
        return render(request,'contact')
