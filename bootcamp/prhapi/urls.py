from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'/', cache_page(60 * 60)(views.get_business_id)),
]