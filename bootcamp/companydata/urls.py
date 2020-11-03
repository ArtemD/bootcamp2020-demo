from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/', views.CompanyList.as_view()),
]