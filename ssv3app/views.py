from django.shortcuts import render, redirect
from .models import Item

def home(request):
    return render(request, 'home.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'ssv3app/item_list.html', {'items': items})  # Notice the 'ssv3app/' before the template name

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item_detail.html', {'item': item})

from .forms import ItemForm

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list after saving
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})
