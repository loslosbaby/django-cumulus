from django.conf import settings

from cumulus.storage import CloudFilesStaticStorage

def cdn_url(request):
    """
    A context processor to expose the full cdn url in templates.

    """
    return {'CDN_URL': settings.CDN_URL}
