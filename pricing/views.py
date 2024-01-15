from django.shortcuts import render
from .models import Pricing
# Create your views here.


def pricing(request):
    pricing = Pricing.objects.all()
    context = {'pricings': pricing}
    return render(request, 'pricing.html', context)
