
from django.conf import settings
from django.contrib.auth.models import User

def global_vars(request):

    global_vars = {
          'WEBSITE_TITLE' : settings.WEBSITE_TITLE
        , 'GIFT_REGISTRY_API_URL' : settings.GIFT_REGISTRY_API_URL
        , 'USER' : request.user
    }

    return global_vars
