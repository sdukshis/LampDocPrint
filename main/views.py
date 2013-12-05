from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.utils.translation import ugettext as _

from main.models import Contractor, Lamp

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

class ContractorList(ListView):
    model = Contractor


class ContractorCreate(CreateView):
    model = Contractor
    def form_valid(self, form):
        messages.success(self.request, _('Successfully saved!'))
        return super(ContractorCreate, self).form_valid(form)


class ContractorUpdate(UpdateView):
    model = Contractor

    def form_valid(self, form):
        messages.success(self.request, _('Successfully saved!'))
        return super(ContractorUpdate, self).form_valid(form)


class ContractorDelete(DeleteView):
    model = Contractor
    success_url = reverse_lazy('contractors')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Object deleted!'))
        return super(ContractorDelete, self).delete(request, *args, **kwargs)


class LampList(ListView):
    model = Lamp


class LampCreate(CreateView):
    model = Lamp

    def form_valid(self, form):
        messages.success(self.request, _('Successfully saved!'))
        return super(LampCreate, self).form_valid(form)


class LampUpdate(UpdateView):
    model = Lamp

    def form_valid(self, form):
        messages.success(self.request, _('Successfully saved!'))
        return super(LampUpdate, self).form_valid(form)


class LampDelete(DeleteView):
    model = Lamp
    success_url = reverse_lazy('contractors')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Object deleted!'))
        return super(LampDelete, self).delete(request, *args, **kwargs)

