from django.shortcuts import render, redirect
from .forms import application_form
from .models import application

# Create your views here.
def create_form(request):
    if request.method == 'POST':
        form = application_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lf')
    else:
        form = application_form()    
    return render(request, 'create.html', {'form': form})
    

def list_form(request):
    items = application.objects.all()
    return render(request, 'list.html', {'items': items})


def update_form(request, pk):
    item = application.objects.get(pk=pk)
    if request.method == 'POST':
        form = application_form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('lf')
    else:
        form = application_form(instance=item)
    return render(request, 'update.html', {'form': form})


def delete_form(request, pk):
    item = application.objects.get(pk=pk)
    if request.method == 'POST':
         item.delete()  
         return redirect('lf')
    return render(request, 'delete.html', {'item': item})         
            
    