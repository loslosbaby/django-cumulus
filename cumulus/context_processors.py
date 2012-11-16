from django.conf import settings

from cumulus.storage import CloudFilesStorage

def cdn_url(request):
    """
    A context processor to expose the full cdn url in templates.

    """
    static_url = settings.STATIC_URL

    if settings.STATICFILES_STORAGE == 'cumulus.storage.CloudFilesStaticStorage':
        cloudfiles_storage = CloudFilesStorage()
        container_url = cloudfiles_storage._get_container_url()
        cdn_url = container_url + static_url
    else:
        cdn_url = static_url

    return {'CDN_URL': cdn_url}