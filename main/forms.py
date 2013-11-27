from django.forms import ModelForm

from main.models import Contractor

class ContractorForm(ModelForm):
    class Meta:
        model = Contractor
        exclude = ('ctime', 'mtime', )
