from .models import *

def social(request):
    social_all = SocialSidebar.objects.all()
    return locals()