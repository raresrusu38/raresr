from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from .models import Education, Experience, MyLanguageSkills

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

    language_RO             = MyLanguageSkills.objects.filter(id=1)
    language_EN             = MyLanguageSkills.objects.filter(id=2)
    language_ES             = MyLanguageSkills.objects.filter(id=3)

    context = {
        'objects_list_edu_one'  : queryset_edu_first,
        'objects_list_edu_two'  : queryset_edu_second,
        'objects_list_exp_one'  : queryset_exp_first,
        'objects_list_exp_two'  : queryset_exp_second,
        'objects_list_exp_three': queryset_exp_third,
        'objects_list_exp_four' : queryset_exp_fourth,
        'objects_list_exp_five' : queryset_exp_fifth,
        'objects_list_exp_six'  : queryset_exp_sixth,
        'objects_list_exp_seven': queryset_exp_seventh,
        'language_RO'           : language_RO,
        'language_EN'           : language_EN,
        'language_ES'           : language_ES,
    }
    return render(request, 'resume.html', context)

def resume_detail(request, id=None):
    queryset = get_object_or_404(Experience, id=id)
    context = {
        'queryset': queryset,
    }
    return render(request, 'resume_detail.html', context)
