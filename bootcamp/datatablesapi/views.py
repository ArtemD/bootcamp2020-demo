from companydata.models import Company
from django_datatables_view.base_datatable_view import BaseDatatableView

class CompanyJson(BaseDatatableView):
    model = Company