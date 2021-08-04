from django.shortcuts import render, redirect

from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
from .models import Stock


# Create your views here.

def home(request):
    title = 'Welcome: This is a stock management system'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def list_item(request):
    header = 'LIST OF ALL ITEM'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()

    context = {
        "header": header,
        "form": form,

    }

    if request.method == 'POST':
        queryset = Stock.objects.filter(category__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value(),
                                        issue_by__icontains=form['issue_by'].value(),
                                        bill_no__icontains=form['bill_no'].value(),

                                        )

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,

        }

    return render(request, "list_item.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method =='POST':
        form=StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)

