from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boombiblico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#--------------------------Despues del login--------------------------------#
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.inicio'),
    url(r'^preguntas/', 'app.views.preguntas'),
    url(r'^nuevapregunta/', 'app.views.nuevapregunta'),
    url(r'^login/', 'app.views.login'),
    url(r'^estadisticas/', 'app.views.estadisticas'),
    url(r'^index/', 'app.views.index'),
)
