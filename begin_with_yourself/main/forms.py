from django import forms

from .models import IdeaModel


class CreateIdea(forms.ModelForm):
    class Meta:

        model = IdeaModel

        fields = ('text', 'scale', 'coordinate_x', 'coordinate_y')
