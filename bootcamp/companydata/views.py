from rest_framework import generics
from . import serializers, models

class CompanyList(generics.ListAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()