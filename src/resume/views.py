from django.shortcuts import render
from .models import Education, Experience

def resume(request):
    queryset_edu_first      = Education.objects.filter(id=1)
    queryset_edu_second     = Education.objects.filter(id=2)

    queryset_exp_first      = Experience.objects.filter(id=1)
    queryset_exp_second     = Experience.objects.filter(id=2)
    queryset_exp_third      = Experience.objects.filter(id=3)
    queryset_exp_fourth     = Experience.objects.filter(id=4)
    queryset_exp_fifth      = Experience.objects.filter(id=5)
    queryset_exp_sixth      = Experience.objects.filter(id=6)
    queryset_exp_seventh    = Experience.objects.filter(id=7)

    context = {
        'objects_list_edu_one'  : queryset_edu_first,
        'objects_list_edu_two'  : queryset_edu_second,
        'objects_list_exp_one'  : queryset_exp_first,
        'objects_list_exp_two'  : queryset_exp_second,
        'objects_list_exp_three': queryset_exp_third,
        'objects_list_exp_four' : queryset_exp_fourth,
        'objects_list_exp_five' : queryset_exp_fifth,
        'objects_list_exp_six'  : queryset_exp_sixth,
        'objects_list_exp_seven' : queryset_exp_seventh,
    }
    return render(request, 'resume.html', context)
