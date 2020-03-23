from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import index, services
from about.views import about
from resume.views import resume, resume_education_detail, resume_experience_detail
from my_portfolio.views import portfolio
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('resume/', resume),
    path('resume/education/<id>/', resume_education_detail, name='resume-education-detail'),
    path('resume/experience/<id>/', resume_experience_detail, name='resume-experience-detail'),
    path('services/', services),
    path('portfolio/', portfolio),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
