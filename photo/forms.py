from django.forms import ModelForm
from .models import *


class EmailForm(ModelForm):
    class Meta:
        model = EmailForm
        fields = '__all__'
