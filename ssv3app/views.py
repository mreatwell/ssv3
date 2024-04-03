from django.shortcuts import render, redirect
from .models import Item
from .forms import UserForm, ProfileForm, YourForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def form_submission_view(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Save the form, e.g., form.save() if it's a ModelForm
            messages.success(request, 'Profile successfully updated.')
            return redirect('success_url')
        else:
            # Log form errors
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = YourForm()

    return render(request, 'your_template.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to a new URL:
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form


    })