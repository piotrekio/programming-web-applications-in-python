from django import forms

from pasta.pastes.models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ('title', 'content')
