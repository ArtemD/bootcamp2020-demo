from django.db import models
from django.utils import timezone

class Company(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, unique=True)
    business_id = models.CharField(max_length=255, unique=True)
    company_form = models.CharField(max_length=255)
    business_line = models.CharField(max_length=255)
    registration_date = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name