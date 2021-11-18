from django.forms import ModelForm
from .models import *


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

