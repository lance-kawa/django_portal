from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User

def home(request: HttpRequest) -> HttpResponse:
    users = User.objects.filter(is_staff=True, is_superuser=False)
    return render(request, 'home.html', {'users': users})

def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    profil = getattr(user, 'profil', None)
    theme = profil.theme.get()
    diplomes = profil.diplomes.order_by('-graduation_date')
    experiences = profil.experiences.order_by('-end_date')
    display_order = theme.category_order.split(', ')
    return render(request, 'portfolio/base.html', {
        'profil': profil, 
        'display_order': display_order, 
        'theme': theme, 
        'diplomes': diplomes,
        'experiences': experiences,
    })

