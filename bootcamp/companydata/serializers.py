from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name','business_id', 'company_form', 'business_line', 'registration_date', 'city', 'address', 'postcode')