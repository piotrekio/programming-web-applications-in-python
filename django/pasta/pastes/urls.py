from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'pasta.pastes.views.home', name='home'),
    url(r'^create/$', 'pasta.pastes.views.create', name='create'),
    url(r'^(?P<unique_id>\w{8,})/$', 'pasta.pastes.views.show', name='show')
]
