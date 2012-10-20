# _*_ coding:utf-8 _*_

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$','messageBoard.views.msg_list_page'),
    url(r'^accounts/register/success/$','django.views.generic.simple.direct_to_template',
            {'template':'registration/register_success.html'}),
    url(r'^accounts/register/fail/$','django.views.generic.simple.direct_to_template',
            {'template':'registration/register_fail.html'}),
    url(r'^accounts/register/$','messageBoard.views.register_page'),
    url(r'^accounts/login/$','django.contrib.auth.views.login'),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^accounts/password/change/$','django.contrib.auth.views.password_change',
            {'template_name':'registration/password_change.html'}),
    url(r'^accounts/password/change/done/$','django.contrib.auth.views.password_change_done',
            {'template_name':'registration/password_change_success.html'}),
    url(r'^accounts/password/reset/$','django.contrib.auth.views.password_reset',
            {'template_name':'registration/password_reset_form.html'}),
    url(r'^accounts/password/reset/done/$','django.contrib.auth.views.password_reset_done',
            {'template_name':'registration/password_reset_done.html'}),
    url(r'^post/$','messageBoard.views.msg_post_page'),
    url(r'^user/(\w+)/$','messageBoard.views.user_msg_list_page'),
    url(r'^detail/(\d+)/$','messageBoard.views.msg_detail_page'),

    #bianjiqi
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':'messageboard/templates/static'}),
    url(r'^detail/site_media/plugins/emotions/img/(?P<path>.*)$',
        'django.views.static.serve',
            {'document_root':'messageboard/templates/static/plugins/emotions/img'}),
    #pinglun
    url(r'^comments/',include('django.contrib.comments.urls')),
    # Examples:
    # url(r'^$', 'messageboard.views.home', name='home'),
    # url(r'^messageboard/', include('messageboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
