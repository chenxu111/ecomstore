from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/$',"ecomstore.views.catalog"),
    url(r'^catalog2/$',"ecomstore.views.catalog2"),
    url(r'^catalog3/$',"preview.views.home"),
)
