from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from .models import MyPortfolio
from pprint import pprint

def portfolio(request, id=None):
    # queryset  = MyPortfolio.objects.filter(id=1)
    queryset_one    = get_object_or_404(MyPortfolio, id=1)
    queryset_two    = get_object_or_404(MyPortfolio, id=2)
    queryset_three  = get_object_or_404(MyPortfolio, id=3)
    queryset_four   = get_object_or_404(MyPortfolio, id=4)


    context = {
        'qs_one'    : queryset_one,
        'qs_two'    : queryset_two,
        'qs_three'  : queryset_three,
        'qs_four'   : queryset_four
    }

    return render(request, 'portfolio.html', context)
