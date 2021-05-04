from django import forms
from .models import Share

class shareForm(forms.ModelForm):

    class Meta:
        model = Share
        fields = ['content']

    def clean_content(self): #clean_content a django compenent
        content = self.cleaned_data.get("content")
        if len(content) > 250:
            raise forms.ValidationError("Commit is to big")
        return content
