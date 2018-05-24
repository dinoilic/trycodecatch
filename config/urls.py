from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from bloodmanager.views import index_admin, index_user, user_overview,\
                               add_donator, my_profile, supply_overview,\
                               send_notification, send_notification_user,\
                               new_donation, user_home, dismiss_notification,\
                               list_events, detail_event, respond_event, add_donation


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    # admin
    url(r'^user_home/$', user_home, name='user_home'),
    url(r'^supply_overview/$', supply_overview, name='supply_overview'),
    url(r'^user_overview/$', user_overview, name='user_overview'),
    url(r'^add_donator/$', add_donator, name='add_donator'),
    url(r'^send_notification/(?P<pk>[\d.@+-]+)/(?P<blood_type>[\w.@+-]+)$', send_notification, name='send_notification'),
    url(r'^dismiss_notification/(?P<pk>[\d.@+-]+)$', dismiss_notification, name='dismiss_notification'),
    url(r'^respond_event/(?P<pk>[\d.@+-]+)/(?P<answer>[\w.@+-]+)$', respond_event, name='respond_event'),
    url(r'^send_notification_user/$', send_notification_user, name='send_notification_user'),
    url(r'^news_donation/$', new_donation, name='new_donation'),
    url(r'^list_events/$', list_events, name='list_events'),
    url(r'^detail_event/(?P<pk>[\d.@+-]+)$', detail_event, name='detail_event'),
    url(r'^add_donation/$', add_donation, name='add_donation'),

    # user
    url(r'^my_donations/$', index_user, name='index_user'),
    url(r'^my_profile/$', my_profile, name='my_profile'),


    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('project_hackathon.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
