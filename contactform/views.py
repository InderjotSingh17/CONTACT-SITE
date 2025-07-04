from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=f'Contact from {contact.name}',
                message=contact.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=False,
            )

            return render(request, 'thanks.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
