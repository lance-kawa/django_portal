from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from itertools import chain
from django.utils.translation import activate
from django.http import HttpResponseRedirect

from cv.models.project.model import Project

def home(request: HttpRequest) -> HttpResponse:
    users = User.objects.filter(is_staff=True).order_by('-id')
    return render(request, 'home.html', {
        'users': users,
    })

def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    profil = getattr(user, 'profil', None)
    diplomes = profil.diplomes.order_by('-graduation_date')
    experiences = profil.experiences.order_by('-end_date')
    display_order = profil.theme.category_order.split(',')
    template_name = 'portfolio/' + username + '/portfolio.html'
    header_name = 'portfolio/' + username + '/header.html'
    return render(request, template_name, {
        'profil': profil, 
        'display_order': display_order, 
        'header_name': header_name,
        'bg_picture': profil.bg_picture.url,
        'cursus': chain(experiences, diplomes)
    })

def change_language(request, lang_code):
    activate(lang_code)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response

def project_view(request: HttpRequest, project_id: str) -> HttpResponse:
    project = Project.objects.get(id=project_id)
    profil = getattr(project, 'profil', None)
    template_name = 'portfolio/' + profil.user.username + '/project.html'
    header_name = 'portfolio/' + profil.user.username + '/header.html'
    return render(request, template_name, {
        'profil': profil, 
        'header_name': header_name,
        'project': project,
    })