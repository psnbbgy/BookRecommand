from django.conf.urls import patterns, include, url
from django.contrib import admin
from CfRecommand import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BookRecommand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', views.hello),
    url(r'^predict/', views.predict),
    url(r'^admin/', include(admin.site.urls)),
)
