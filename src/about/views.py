from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from .models import AboutMe

def about(request, id=None):
    queryset = get_object_or_404(AboutMe, id=1)
    print(queryset)

    context = {
        'qs': queryset,
    }

    return render(request, 'about-us.html', context)
