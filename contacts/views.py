from django.shortcuts import render, get_object_or_404, reverse
from .models import Feedback, FeedbackCategory
from index.models import Section
from .models import FeedbackCategory
from django.http import HttpResponseRedirect
from django.conf import settings
import requests


def render_contacts_page(request):
    first_section = Section.objects.get(order=1)
    second_section = Section.objects.get(order=2)
    third_section = Section.objects.get(order=3)
    fourth_section = Section.objects.get(order=4)

    categories = FeedbackCategory.objects.all()

    context = {
        'first_section': first_section,
        'second_section': second_section,
        'third_section': third_section,
        'fourth_section': fourth_section,
        'categories': categories
    }
    return render(request, 'contacts/contacts.html', context)


def feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'anonymous')
        name = request.POST.get('name', 'anonymous')
        phone = request.POST.get('phone', '')
        category = FeedbackCategory.objects.get(pk=request.POST.get('category'))
        content = request.POST.get('content', '')

        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_CAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:
            Feedback.objects.create(
                name=name,
                email=email,
                phone=phone,
                category=category,
                content=content
            )
            return HttpResponseRedirect(reverse('contacts'))
        else:
            return HttpResponseRedirect(reverse('contacts'))
