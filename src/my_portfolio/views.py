from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from .models import MyPortfolio
from pprint import pprint

def portfolio(request, id=None):
    # queryset  = MyPortfolio.objects.filter(id=1)
    queryset = get_object_or_404(MyPortfolio, id=1)

    pprint(queryset)

    context = {
        'qs': queryset,
    }

    return render(request, 'portfolio.html', context)
