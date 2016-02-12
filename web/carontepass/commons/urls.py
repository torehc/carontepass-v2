from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^index.html$', TemplateView.as_view(template_name="commons/index.html")),
    url(r'^login.html$', TemplateView.as_view(template_name="commons/login.html")),
]