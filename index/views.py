from django.shortcuts import render
from .models import Section, Category


def render_index(request):
    first_section = Section.objects.get(order=1)
    second_section = Section.objects.get(order=2)
    third_section = Section.objects.get(order=3)
    fourth_section = Section.objects.get(order=4)

    print(first_section.get_categories().first().get_album().get_images().first())

    context = {
        'first_section': first_section,
        'second_section': second_section,
        'third_section': third_section,
        'fourth_section': fourth_section
    }
    return render(request, 'index/index.html', context)
