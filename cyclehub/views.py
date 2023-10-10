from django.http import HttpResponse
from django.template import loader
from .models import Item
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, ItemForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print("Form data is cleaned:", cd)
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    print("User account is deactivated.")
                    return render(request, 'login.html', {'form': form, 'error': 'This account is deactivated.'})
            else:
                print("Authentication failed.")
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
        else:
            print("Form is not valid:", form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def items(request):
    myitems = Item.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

@login_required
def details(request, id): 
    myitem = Item.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myitem': myitem,
    }
    return HttpResponse(template.render(context, request))

@login_required
def main(request): 
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def testing(request): 
    myitems = Item.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))
    
@login_required
def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.itemowner = request.user
            item.save()
            return render(request, 'item_added.html', {'myitems': Item.objects.all()})
        else:
            return render(request, 'add_item.html', {'form': form})
    return render(request, 'add_item.html', {'form': form})

@login_required
def item_added(request):
    return render(request, 'item_added.html')
