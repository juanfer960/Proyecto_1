from django.forms import ModelForm
from django import forms
from .models import SiteProjects


class SiteProjectsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SiteProjectsForm, self).__init__(*args, **kwargs)
        self.fields['prj_creationdate'].widget.attrs['readonly'] = True

    class Meta:
        model = SiteProjects
        fields = ('prj_name', 'prj_description', 'prj_budget', 'prj_creationdate')
