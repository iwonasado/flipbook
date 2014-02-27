from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

admin.autodiscover()
handler500 = 'meucatalogovirtual.views.server_error'
handler404 = 'django.views.defaults.page_not_found'
handler403 = 'django.views.defaults.permission_denied'

urlpatterns = patterns(
    '',
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')), 
    url(r'^catalogos/(?P<slug>\w+)/$', 'flipbook.views.inicial',name="catalogos"),
    url(r'^catalogos/(?P<slug>\w+)/flipbook/$', 'flipbook.views.flipbook'),
    url(r'^criar-catalogo/', 'flipbook.views.create'),
    url(r'^login/', 'account.views.mylogin', name='login'),
    url(r'^logout/', 'account.views.logout',name='logout'),
    url(r'^registrar/', 'account.views.registrar',name='registrar_usuario'),
    url(r'^avaiable/user/$', 'account.views.avaiableUser',name='avaiable_user'),
    url(r'^avaiable/email/$', 'account.views.avaiableEmail',name='avaiable_email'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
)

urlpatterns += patterns(
    '',
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'meucatalogovirtual.views.server_error'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += patterns(
    '',
    url(r'^', include('cms.urls')),
)
