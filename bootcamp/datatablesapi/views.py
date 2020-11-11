from companydata.models import Company
from django_datatables_view.base_datatable_view import BaseDatatableView

class CompanyJson(BaseDatatableView):
    model = Company

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__icontains=search)
        return qs