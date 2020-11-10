from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CompanyForm
from .prhlib import get_company_info

def get_business_id(request):
    info = None
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = get_company_info(form.cleaned_data['business_id'])
            if company:
                info = company
            else:
                info = 'It didn\' work. Did you input correct business id?' 
    else:
        form = CompanyForm()

    return render(request, 'form.html', {'form': form, 'info': info})