from django.contrib import admin

from .models import Education, Experience, MyLanguageSkills, MyTechnicalSkills

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(MyLanguageSkills)
admin.site.register(MyTechnicalSkills)
