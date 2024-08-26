from django.shortcuts import render, redirect
from .forms import SaleForm
from django.contrib import messages

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