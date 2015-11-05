from django.conf import settings
from django.shortcuts import render
from localflavor.us.models import STATE_CHOICES

from .models import Campaign

#
# def gen_template_name(campaign):
#     # template = gen_template_name(LP_version)
#     return 'templates/index{}.html'.format(Campaign['campaign'-1].LP_version)
#
#
# def home(request, campaign):
#     template = gen_template_name(Campaign.LP_version)
#     # template = 'index1.html'
#     context = {
#         'campaign': Campaign.objects.all()[0],
#     }
#     return render(request, template, context)


def gen_template_name(campaign):
    return 'index{}.html'.format(Campaign.objects.get([1]).LP_version)


def home(request, campaign):
    template = gen_template_name(campaign)
    context = {
        'campaign': Campaign.objects.all(),
        'data': request.GET
    }
    return render(request, template, context)

