from django import forms
from .models import pollmodel
class pollforms(forms.ModelForm):
    class Meta:
        model = pollmodel
        fields = ['poll_question','poll_option_one','poll_option_two','poll_option_three']