from django.http import HttpResponse
from django.template import loader
from .models import Item

def items(request):
    myitems = Item.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

def details(request, id): 
    myitem = Item.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myitem': myitem,
    }
    return HttpResponse(template.render(context, request))

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