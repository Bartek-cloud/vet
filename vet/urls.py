from django.conf import settings
from django.template.defaulttags import url
from django.urls import include, path, re_path
from django.contrib import admin
from schedule.views import api_occurrences, CreateEventView
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as crx_admin_urls
from coderedcms import search_urls as crx_search_urls
from coderedcms import urls as crx_urls
from schedule_wagtail import urls as schedule_urls
from veter import urls as veter_urls
from wagtail import urls as wagtail_urls
urlpatterns = [
    # Admin
    path("django-admin/", admin.site.urls),
    path("admin/", include(crx_admin_urls)),
    # Documents
    path("docs/", include(wagtaildocs_urls)),
    # Search
    path("search/", include(crx_search_urls)),
    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:
    path("", include('allauth.urls')),
    #url(r'', include(wagtail_urls)),
    path("", include(crx_urls)),
    path("", include(schedule_urls)),
    path("", include(schedule_urls)),
    # Alternatively, if you want pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(crx_urls)),
    path("", include(wagtail_urls)),
    #path("", 'api/occurrences/calendar_slug=<calendar_slug>&start=<start_date>&end=<end_date>', api_occurrences, name='api_occurrences'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
