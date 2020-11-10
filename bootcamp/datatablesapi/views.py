from companydata.models import Company
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.cache import cache_page

@cache_page(60 * 60)
class CompanyJson(BaseDatatableView):
    model = Company

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)
        return qs