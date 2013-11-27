from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from main.models import Contractor
from main.forms import ContractorForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_contractor(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_contractor)
    else:
        form = ContractorForm()
    return render(request, 'contractor.html', {'form': form})

@login_required
def contractor(request, id=None):
    contractor = get_object_or_404(Contractor, pk=id)
    form = ContractorForm(instance=contractor)
    return render(request, 'contractor.html', {'form': form})

@login_required
def list_contractor(request):
    contractors = Contractor.objects.all()
    return render(request, 'contractor_list.html', {'contractors': contractors})
