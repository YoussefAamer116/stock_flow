from datetime import datetime
from django.shortcuts import render, redirect
from .forms import SaleForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Sale
from django.template.loader import get_template
import weasyprint

# Create your views here.

def sell_item(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Item sold successfully!')
                return redirect('stock_page')
            except ValueError as e:
                form.add_error(None, str(e))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SaleForm()
    return render(request, 'sell_item.html', {'form': form})


def sales_report(request):
    sales = Sale.objects.all()
    current_datetime = datetime.now()
    template = get_template('sales_report.html')
    html = template.render({'sales': sales, 'current_datetime': current_datetime})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
