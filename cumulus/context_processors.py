from django.conf import settings

from cumulus.storage import CloudFilesStaticStorage

def cdn_url(request):
    """
    A context processor to expose the full cdn url in templates.

    """
    static_url = settings.STATIC_URL

    if settings.STATICFILES_STORAGE == 'cumulus.storage.CloudFilesStaticStorage' and not settings.DEBUG:
        #cloudfiles_storage = CloudFilesStaticStorage()
        #container_url = cloudfiles_storage._get_container_url()
        #cdn_url = container_url + static_url
        cdn_url = 'https://3fe98249bc30b3d0113c-8e627ca5b66feb89c2661eae1a2cc475.ssl.cf2.rackcdn.com/static/'
    else:
        cdn_url = static_url

    return {'CDN_URL': cdn_url}